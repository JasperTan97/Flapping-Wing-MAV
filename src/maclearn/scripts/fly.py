#!/usr/bin/env python3
# ros and lib imports
import rospy
import message_filters
from geometry_msgs.msg import PoseStamped, TwistStamped, AccelStamped
from custommsg.msg import ppmchnls
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
training_name = "insert_training_name_here"
# Specify the Algorithm/Model to use
model = "DDPG" # 'MAA2C', 'MAD3QN' --> multi-agent approch OR 'A2C_MultiAction', 'A2C_SingleAction', 'DDPG' --> single-agent approach
# Specify number of Episodes to run for
episodes = 10
# Action Space (number of channels output)
action_space = 4
# State Space
state_space = 19
# min and max PPM value (microsec)
min_PPM = 1100
max_PPM = 1900
# Do you want to save the best versions of the model?
save_best_model = True
# Do you want to save the CSV data from training?
save_data = True
#set mode (test, load_n_train or train)
mode = "train"
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
move_up_dist = 2 # in metres
max_sideways_radius = 1 # in metres

# file paths to save replay data
try:
	os.mkdir('../replay_data/' + goal_mode + "_" + goal_instance)
except:
	check = input("The instance {} of goal {} already exists, do you want to build on this replay data? (y/n)".format(goal_instance, goal_mode))
	if (check.lower() == 'y'):
		pass
	else:
		while(True):
			goal_instance = str(int(goal_instance) + 1)
			try:
				os.mkdir('../replay_data/' + goal_mode + "_" + goal_instance)
				"A separate directory of {}_{} has been created".format(goal_mode, goal_instance)
			except:
				pass

file_list = ['../replay_data/' + goal_mode + "_" + goal_instance] * 5
file_list[0] += '/state.csv'
file_list[1] += '/state_prime.csv'
file_list[2] += '/action.csv'
file_list[3] += '/reward.csv'
file_list[4] += '/terminal.csv'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ GLOBAL VARIABLES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# make global agent
agent = Agent(model, discount_rate, lr_actor, lr_critic, action_space, tau, max_mem_size, batch_size, noise,
	max_action, min_action, update_target, training_name, state_space)
# make global publisher
pub_arduino = rospy.Publisher('channel_values_time', ppmchnls, queue_size=10)
# starting x,y,z coordinates & setter bool
start_x, start_y, start_z = 0, 0, 0
first_msg = True
# global np state array and prev_action
state = []
prev_action = tf.zeros((action_space))
episode_is_done = False

# load saved models if testing
if mode == "test" or mode == "load_n_train":
	agent.load_all_models()

if mode == "load_n_train" 

def check_is_done(state_prime):
	""" function to check of goal has been reached """

	# termination check (within radius)
	if (pow(state_prime[0], 2) + pow(state_prime[1], 2) > pow(max_sideways_radius, 2)):
		return True

	if goal_mode == "move_up"
		if state_prime[2] > move_up_dist:
			return True
	return False

def return_reward(state, state_prime):
	""" function to determine reward """
	if goal_mode == "move_up":
		# difference in upward velocity (positive is better)
		return state_prime[9] - state[9] - (move_up_dist - state_prime[2])

def callback(pose, twist, accel): # rmb to normalise

	# record the starting x,y,z coordinate of the MAV
	if first_msg:
		start_x, start_y, start_z = pose.pose.position.x, pose.pose.position.y, pose.pose.position.z

	# use the ROS callback to get the 19 states (via VICON)
	state_prime = [pose.pose.position.x - start_x, pose.pose.position.y - start_y, pose.pose.position.z - start_z,
	pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w,
	twist.twist.linear.x, twist.twist.linear.y, twist.twist.linear.z, twist.twist.angular.x, twist.twist.angular.y,
	twist.twist.angular.z, accel.accel.linear.x, accel.accel.linear.y, accel.accel.linear.z, accel.accel.angular.x,
	accel.accel.angular.y, accel.accel.angular.z]

	# get the action (scale [-1,1] to [1100, 1900])
	action = agent.select_actions(state_prime, mode) * 0.5*(max_PPM - min_PPM) + 0.5*(min_PPM + max_PPM)

	# see if the episode goal has been reached or the flight failed
	episode_is_done = check_is_done(state_prime)

	# create chnl msg
	chnl_msg = ppmchnls()

	if episode_is_done:
		# MIGHT CHANGE
		# FAILSAFE MODE
		chnl_msg.chn1=chnl_msg.chn2=chnl_msg.chn3=chnl_msg.chn4=chnl_msg.chn5=chnl_msg.chn6=chnl_msg.chn7=chnl_msg.chn8 = min_PPM
			if save_data:
				agent.memory.save_replay_buffer()
	else:
		# PUBLISH TO CHANNELS (HARDCODED FOR DUAL MOTOR  + DUAL SERVO MAV)
		chnl_msg.chn1 = action[0]
		chnl_msg.chn2 = action[1]
		chnl_msg.chn3 = action[2]
		chnl_msg.chn4 = action[3]
		chnl_msg.chn5, chnl_msg.chn6, chnl_msg.chn7, chnl_msg.chn8 = min_PPM

	pub_arduino.publish(chnl_msg)

	# set current state_prime to state and action to prev_action and return as we cannot 
	if first_msg:
		state = np.copy(state_prime)
		prev_action = np.copy(action)
		first_msg = False
		return

	agent.store_memory(state, action_prev, return_reward(state, state_prime), state_prime, episode_is_done)

	state = state_prime[:]
	prev_action = np.copy(action)

def fly():

	# initialise node and subscribers
	rospy.init_node('bird_data_compiler_node_py', anonymous=True)
	sub_vicon_pose = message_filters.Subscriber('/mavros/vision_pose/pose', PoseStamped)
	sub_vicon_twist = message_filters.Subscriber('/vrpn_client_node/flapusp/twist', TwistStamped)
	sub_vicon_accel = message_filters.Subscriber('/vrpn_client_node/flapusp/accel', AccelStamped)

	# synchronize topics
	ts = message_filters.ApproximateTimeSynchronizer([sub_vicon_pose, sub_vicon_twist,sub_vicon_accel], 10, 0.1, allow_headerless=True)

	# register callback
	ts.registerCallback(callback)
	
	# rate = rospy.Rate(2) # 10hz
	nn_training_loss_log = []

	while not rospy.is_shutdown():
		for episode in range(episodes):
			rospy.info("COMMENCING EPISODE {}".format(episode + 1))
			while not episode_is_done:
		        if agent.model == "DDPG":
			        nn_training_loss_log.append(agent.apply_gradients_DDPG())
			        # nn_training_episode_log.append(x+1)
			else:

		# rate.sleep()
	if save_data:
		agent.memory.save_replay_buffer()



#if __name__ == "__main__":
fly()
