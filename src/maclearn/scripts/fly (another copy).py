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

# define parameters
# SPECIFY TRAINING NAME
training_name = "insert_training_name_here"
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

agent = Agent(model, discount_rate, lr_actor, lr_critic, action_space, tau, max_mem_size, batch_size, noise, max_action, min_action, update_target, training_name, state_space)
a = 0
"""
def callback(pose, twist, accel, ppm): # rmb to normalise
    pass
"""

def callback(ppm): # rmb to normalise
    global a
    #a+= 1
    rospy.loginfo("callback a: {}".format(a))
    
def fly():

    # initialise node and subscribers
    rospy.init_node('bird_data_compiler_node_py', anonymous=True)

    sub_vicon_pose = message_filters.Subscriber('/mavros/vision_pose/pose', PoseStamped)
    sub_vicon_twist = message_filters.Subscriber('/vrpn_client_node/flapusp/twist', TwistStamped)
    sub_vicon_accel = message_filters.Subscriber('/vrpn_client_node/flapusp/accel', AccelStamped)
    sub_arduino = message_filters.Subscriber('channel_values_time', ppmchnls)
    """
    ts = message_filters.ApproximateTimeSynchronizer([sub_vicon_pose, sub_vicon_twist,                sub_vicon_accel], 10, 0.1, allow_headerless=True)
    """
    ts = message_filters.ApproximateTimeSynchronizer([sub_arduino], 10, 0.1, allow_headerless=True) 
    
    ts.registerCallback(callback)
    # start fly function

    
    # rate = rospy.Rate(2) # 10hz
    
    global a

    while not rospy.is_shutdown():
        for i in range(100000):
            a = yomum(a)
        # a+= 1
        rospy.loginfo("main a: {}".format(a))
        # rospy.loginfo("im workinggggg :)")
        # rate.sleep()

    # rospy.spin()



#if __name__ == "__main__":
fly()
