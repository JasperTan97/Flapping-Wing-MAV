""" 
This source code file contains the code for the replay_buffer class
Purpose 1: store memory of state, action, state_prime, reward, terminal flag 
Purpose 2: function to randomly sample a batch of memory
"""

# Standard Imports
import numpy as np
from numpy import genfromtxt

class replay_buffer:
    
    def __init__(self, max_mem_size, state_input_shape, action_space):
        
        """ class constructor that initialises memory states attributes """
        
        # bound for memory log
        self.mem_size = max_mem_size
        
        # counter for memory logged
        self.mem_counter = 0 
        
        # logs for state, action, state_prime, reward, terminal flag
        self.state_log = np.zeros((self.mem_size, *state_input_shape))
        self.state_prime_log = np.zeros((self.mem_size, *state_input_shape))
        
        if action_space != 1:
            
            self.action_log = np.zeros((self.mem_size, action_space))
        
        else:
            
            self.action_log = np.zeros(self.mem_size)
            
        self.reward_log = np.zeros(self.mem_size)
        self.terminal_log = np.zeros(self.mem_size)
        
    def log(self, state, action, reward, state_prime, is_done):
        
        """ log memory """
        
        # index for logging. based on first in first out
        index = self.mem_counter % self.mem_size
        
        # log memory for state, action, state_prime, reward, terminal flag
        
        
        self.state_log[index] = state
        self.state_prime_log[index] = state_prime
        self.action_log[index] = action
        self.reward_log[index] = reward
        self.terminal_log[index] = is_done

        # increment counter
        self.mem_counter += 1
    
    def sample_log(self, batch_size):
        
        """ function to randomly sample a batch of memory """
        
        # select amongst memory logs that is filled
        max_mem = min(self.mem_counter, self.mem_size)
        
        # randomly select memory from logs
        batch = np.random.choice(max_mem, batch_size, replace = False)
        
        # obtain corresponding state, action, state_prime, reward, terminal flag
        states = self.state_log[batch]
        states_prime = self.state_prime_log[batch]
        actions = self.action_log[batch]
        rewards = self.reward_log[batch]
        is_dones = self.terminal_log[batch]

        # CAN ADD CODE FOR NORMALISE
        
        return states, actions, rewards, states_prime, is_dones

    def load_replay_buffer(self, file_list):
        
        """ function that takes in list of csv file paths to extract replay buffer """ 
        
        # create empty list to store replay buffer extracted
        replay_buffers = []
        
        # iterate over elements of the replay buffer
        for x in range(len(file_list)):
        
            # open CSV file to get corresponding data and append to repaly_buffers
            replay_buffers.append(np.genfromtxt(file_list[x], skip_header=1))
            
        # update state, action, state_prime, reward, terminal flag to replay_buffer
        self.state_log = replay_buffers[0]
        self.state_prime_log = replay_buffers[1]
        self.action_log = replay_buffers[2]
        self.reward_log = replay_buffers[3]
        self.terminal_log = replay_buffers[4]
        
    def save_replay_buffer(self, file_list):
	
        """ function that takes in list of csv file paths to save replay buffer """ 
         
        # save the elements of replay buffer to csv files
        np.savetxt(file_list[0], self.state_log[:self.mem_counter % self.mem_size], delimiter=',')
        np.savetxt(file_list[1], self.state_prime_log[:self.mem_counter % self.mem_size], delimiter=',')
        np.savetxt(file_list[2], self.action_log[:self.mem_counter % self.mem_size], delimiter=',')
        np.savetxt(file_list[3], self.reward_log[:self.mem_counter % self.mem_size], delimiter=',')
        np.savetxt(file_list[4], self.terminal_log[:self.mem_counter % self.mem_size], delimiter=',')

