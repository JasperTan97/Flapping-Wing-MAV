#!/usr/bin/env python3
# ros and lib imports
import rospy
import message_filters
from geometry_msgs.msg import PoseStamped, TwistStamped, AccelStamped
from custommsg.msg import ppmchnls
from custommsg.msg import kinematicstamped
from NeuralNetwork import *
from ReplayBuffer import *
from BirdAgent import *

# Standard Imports
import pandas as pd
import numpy as np
import math
import time
import os
import shutil

# define parameters
# SPECIFY TRAINING NAME
training_name = "debugging"
# Specify the Algorithm/Model to use
model = "DDPG" # 'MAA2C', 'MAD3QN' --> multi-agent approch OR 'A2C_MultiAction', 'A2C_SingleAction', 'DDPG' --> single-agent approach
# Specify number of Episodes to run for
episodes = 1
# Action Space (number of channels output)
action_space = 4
# State Space
state_space = 19
# Do you want to save the best versions of the model?
save_best_model = True
# Do you want to save the CSV data from training?
save_data = True
# set mode (test, load_n_train or train)
mode = "train"
#~~~~~~~~~~~~~~~~~~~~~~~~ PARAMETERS FOR BIRD TRAINING ~~~~~~~~~~~~~~~~~~~~~~~~~~#
# min and max PPM value (microsec)
min_PPM = np.array([1100, 1100, 1450, 1330])
max_PPM = np.array([1900, 1900, 1780, 1800])
dead_PPM = 1100
failsafe_PPM = [1100, 1100, int(0.5*(min_PPM[2] + max_PPM[2])), 
int(0.5*(min_PPM[3] + max_PPM[3])), dead_PPM, dead_PPM, dead_PPM, dead_PPM]
# height of ceiling above starting location
ceiling_height = 2.7 # in metres
# max radius of free movement
free_rad = 2.6 # in metres, total length = 2.7
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ HYPERPARAMETER CONFIG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Specify learning rates for actors and critics, for MAD3QN, only the actor learning rate is used
lr_actor = 0.00005
lr_critic = 0.0001
# Specify the discount rate
discount_rate = 0.9
# number of time_steps to do a hard copy for target networks in MAD3QN and DDPG 
# Otherwise enter None for Softcopy
update_target = None
# Tau value for soft copy of online network weights to target networks for MAD3QN and DDPG
tau = 0.005
# Replay memory size and batch size for MAD3QN and DDPG
max_mem_size = 1000000
batch_size = 512
# Continuous action space range in units of rad/s of joints and noise stddev for DDPG.
max_action = 1
min_action = -1
noise = 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ REWARD STRUCTURE CONFIG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# possible reward_modes: move_up
goal_mode = "move_up"
# the instance of training for the same goal (if I want to separate replay buffers)
goal_instance = "1"
move_up_dist = 1.2 # in metres
max_sideways_radius = 2.2 # in metres
time_limit = 150 #np.inf # in seconds (set to infinity first as we dont wanna activate this temrination yet)

dirname = os.path.dirname(__file__)

# file paths to save replay data
try:
	os.mkdir(os.path.join(dirname, '../replay_data/' + training_name + "_" + goal_mode + "_" + goal_instance))
except:
	check = input("The instance {} of goal {} already exists, do you want to build on this replay data? (y/n)".format(goal_instance, goal_mode))
	if (check.lower() == 'y'):
		pass
	else:
		while(True):
			goal_instance = str(int(goal_instance) + 1)
			try:
				os.mkdir(os.path.join(dirname, '../replay_data/' + training_name + "_" + goal_mode + "_" + goal_instance))
				"A separate directory of {}_{} has been created".format(goal_mode, goal_instance)
				break
			except:
				pass

file_list = [os.path.join(dirname, '../replay_data/' + training_name + "_" + goal_mode + "_" + goal_instance)] * 5
file_list[0] += '/state.csv'
file_list[1] += '/state_prime.csv'
file_list[2] += '/action.csv'
file_list[3] += '/reward.csv'
file_list[4] += '/terminal.csv'

training_name = training_name + "_" + goal_mode + "_" + goal_instance

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ GLOBAL VARIABLES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
agent = Agent(model, discount_rate, lr_actor, lr_critic, action_space, tau, max_mem_size, batch_size, noise,
	max_action, min_action, update_target, training_name, state_space)
start_x, start_y, start_z = 0, 0, 0
first_msg = True
start_time = 0
pub_arduino = rospy.Publisher('channel_values_arduino', ppmchnls, queue_size=10)
state = []
prev_action = tf.zeros((action_space))
episode_is_done = 0
best_time = np.inf
buffer_saved = True


# load saved models if testing
if mode == "test" or mode == "load_n_train":
	agent.load_all_models()

# load replay_buffer
if mode == "load_n_train":
	agent.memory.load_replay_buffer(file_list)

def check_is_done(state_prime, time_taken):
	""" function to check of goal has been reached """

	# termination check (within radius of cylinder)
	if (pow(state_prime[0], 2) + pow(state_prime[1], 2) > pow(max_sideways_radius, 2)):
		rospy.loginfo("Bird has exceeded maximum radius of {}m".format(max_sideways_radius))
		return 2

	# termination check (takes too long)
	if (time_taken > time_limit):
		rospy.loginfo("Bird has exceeded time limit of {}s".format(time_limit))		
		return 3

	# termination check (within radius of hemisphere of string)
	#if (pow(state_prime[0], 2) + pow(state_prime[1], 2) + pow(state_prime[2] + ceiling_height, 2) > pow(free_rad, 2)):
	#	print("4")

	#	return 4

	if goal_mode == "move_up":
		if state_prime[2] > move_up_dist:
			rospy.loginfo("BIRD HAS REACHED GOAL HEIGHT OF {}m after {}s".format(move_up_dist, time_taken))
			return 1
	return 0

def return_reward(state, state_prime):
	""" function to determine reward """
	if goal_mode == "move_up":
		# difference in upward velocity (positive is better)
		return state_prime[9] - state[9] - (move_up_dist - state_prime[2])

def callback(kinematics): # rmb to normalise

	global first_msg, pub_arduino, failsafe_PPM, dead_PPM, episode_is_done, start_x, start_y, start_z, start_time, state, prev_action, best_time, buffer_saved, save_best_model, save_data
	#rate2 = rospy.Rate(10)
	#while True:	
		

	# record the starting x,y,z coordinate of the MAV
	if first_msg:
		start_time = time.time()
		start_x, start_y, start_z = kinematics.pose.position.x, kinematics.pose.position.y, kinematics.pose.position.z

	# use the ROS callback to get the 19 states (via VICON)
	state_prime = [kinematics.pose.position.x - start_x, kinematics.pose.position.y - start_y, kinematics.pose.position.z - start_z,
	kinematics.pose.orientation.x, kinematics.pose.orientation.y, kinematics.pose.orientation.z, kinematics.pose.orientation.w,
	kinematics.twist.linear.x, kinematics.twist.linear.y, kinematics.twist.linear.z, kinematics.twist.angular.x, kinematics.twist.angular.y,
	kinematics.twist.angular.z, kinematics.accel.linear.x, kinematics.accel.linear.y, kinematics.accel.linear.z, kinematics.accel.angular.x,
	kinematics.accel.angular.y, kinematics.accel.angular.z]

	# get the action (scale [-1,1] to [min_PPM, max_PPM])
	action = agent.select_actions(state_prime, mode) * 0.5*(max_PPM - min_PPM) + 0.5*(min_PPM + max_PPM)

	# see if the episode goal has been reached or the flight failed (only check if episode is not already done)
	if not episode_is_done:
		episode_is_done = check_is_done(state_prime, time.time() - start_time)

	# create chnl msg
	chnl_msg = ppmchnls()

	if episode_is_done:
		if save_data:
			buffer_saved = False

		# FAILSAFE MODE
		chnl_msg.chn1,chnl_msg.chn2,chnl_msg.chn3,chnl_msg.chn4,chnl_msg.chn5,chnl_msg.chn6,chnl_msg.chn7,chnl_msg.chn8 = failsafe_PPM
		
		if save_data:
			agent.memory.save_replay_buffer(file_list)
			buffer_saved = True
			save_data = False

		if save_best_model:
			if (episode_is_done and time.time() - start_time < best_time):
				best_time = time.time() - start_time
				agent.save_all_models()
				save_best_model = False


	else:
		# PUBLISH TO CHANNELS (HARDCODED FOR DUAL MOTOR  + DUAL SERVO MAV)
		chnl_msg.chn1 = int(action[0])
		chnl_msg.chn2 = int(action[1])
		chnl_msg.chn3 = int(action[2])
		chnl_msg.chn4 = int(action[3])
		chnl_msg.chn5=chnl_msg.chn6=chnl_msg.chn7=chnl_msg.chn8 = dead_PPM

	pub_arduino.publish(chnl_msg)

	# set current state_prime to state and action to prev_action and return as we cannot 
	if first_msg:
		state = np.copy(state_prime)
		prev_action = np.copy(action)
		first_msg = False
		return

	# only store memory if episode is running
	if not episode_is_done:
		agent.store_memory(state, prev_action, return_reward(state, state_prime), state_prime, episode_is_done)

		state = state_prime[:]
		prev_action = np.copy(action)

			
	#rospy.loginfo("Cb")
	#rate2.sleep()
	#break

def ros_fly():

	# initialise node and subscribers
	rospy.init_node('bird_data_compiler_node_py', anonymous=True, disable_signals = True)
	# sub_vicon_pose = message_filters.Subscriber('/mavros/vision_pose/pose', PoseStamped)
	# sub_vicon_twist = message_filters.Subscriber('/vrpn_client_node/flapusp/twist', TwistStamped)
	# sub_vicon_accel = message_filters.Subscriber('/vrpn_client_node/flapusp/accel', AccelStamped)

	# # synchronize topics
	# ts = message_filters.ApproximateTimeSynchronizer([sub_vicon_pose, sub_vicon_twist,sub_vicon_accel], 10000, 0.1, allow_headerless=True)

	# # register callback
	# ts.registerCallback(callback)

	rospy.Subscriber("ThreeinOneKinematics", kinematicstamped, callback)
	
	rate = rospy.Rate(2) # 10hz
	nn_training_loss_log = []

	global episode_is_done, first_msg, buffer_saved, save_best_model, save_data, failsafe_PPM

	while not rospy.is_shutdown():
		for episode in range(episodes):
			rospy.loginfo("COMMENCING EPISODE {}".format(episode + 1))
			try:
				while not episode_is_done:
					if agent.model == "DDPG" and mode != "test":
						nn_training_loss_log.append(agent.apply_gradients_DDPG())
					rate.sleep()
				rospy.loginfo("The training for episode {} has terminated, Buffer is loading...".format(episode+1))
				while not buffer_saved:
					pass
				if episode < episodes - 1:
					check = input("Buffer saved! Reset bird and press any key to continue\n")
				first_msg = True
				episode_is_done = 0
				save_data = True
				save_replay_buffer = True
			except KeyboardInterrupt:
				save_data = False
				save_best_model = False
				episode_is_done = 99
				agent.memory.save_replay_buffer(file_list)
				if episode < episodes - 1:
					check = input("The training for episode {} has terminated, reset bird and press any key to continue".format(episode+1))
				first_msg = True
				episode_is_done = 0
				save_data = True
				save_replay_buffer = True
		break
		# rate.sleep()
	if save_data:
		agent.memory.save_replay_buffer(file_list)

	# FAILSAFE MODE AFTER TRAINING ENDS
	chnl_msg = ppmchnls()
	chnl_msg.chn1,chnl_msg.chn2,chnl_msg.chn3,chnl_msg.chn4,chnl_msg.chn5,chnl_msg.chn6,chnl_msg.chn7,chnl_msg.chn8 = failsafe_PPM
	pub_arduino.publish(chnl_msg)
	rospy.loginfo("Training has ended")

#if __name__ == "__main__":
ros_fly()


## penalty for going out of range
## but must put ppm back in
## 