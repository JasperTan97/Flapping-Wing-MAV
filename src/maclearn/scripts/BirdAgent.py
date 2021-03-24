# Standard Imports
import tensorflow as tf
import numpy as np
import os
# ME5406 Imports
from NeuralNetwork import fc_model
from ReplayBuffer import replay_buffer 

""" 
Agent class 
Purpose 1 : creates and updates neural network 
Purpose 2 : processes output from neural network to decide action for p_gym
5 Algorithms available: MAD3QN, MAA2C, A2CMA, A2CSA, DDPG
"""

class Agent:
    
    def __init__(self, model, discount_rate, lr_actor, lr_critic, action_space, tau, max_mem_size, batch_size, noise, max_action, min_action, update_target, training_name, state_space):
        
        """ class constructor that initialises discount rate for critic loss, learning rate for actor and critic """
        """ as well as the neural network models for actor and critic """
        
        self.model = model
        
        # stores state space
        self.state_space = state_space
        
        # discount rate for critic loss (TD error)
        self.discount_rate = discount_rate
        
        # learning rate for actor model
        self.lr_actor = lr_actor
        
        # learning rate for critic model
        self.lr_critic = lr_critic
        
        # stores action space
        self.action_space = action_space
        
        if self.model == "DDPG":
            
            # softcopy parameter for target network 
            self.tau = tau

            # counter for apply gradients
            self.apply_grad_counter = 0 
            
            # step for apply_grad_counter to hardcopy weights of original to target
            self.update_target = update_target
            
            # memory for replay
            self.memory = replay_buffer(max_mem_size, [self.state_space], self.action_space)
            
            # batch of memory to sample
            self.batch_size = batch_size
            
            # noise for action
            self.noise = noise
            
            # upper and lower bounds for actions
            self.max_action = max_action
            self.min_action = min_action
            
            # intialise actor model
            self.DDPG_Actor = fc_model(model = "DDPG_Actor", 
                                  h_units = [512, 256, 128], 
                                  weight_decay = [0, 0, 0], dropout_rate = [0, 0, 0], 
                                  num_of_outputs = self.action_space, training_name = training_name)
            
            # update actor model_names attributes for checkpoints
            self.DDPG_Actor.model_name = "DDPG_Actor"

            # update actor checkpoints_path attributes
            self.DDPG_Actor.checkpoint_path = os.path.join(self.DDPG_Actor.checkpoint_dir, self.DDPG_Actor.model_name)
            
            # intialise target actor model
            self.DDPG_Target_Actor = fc_model(model = "DDPG_Actor", 
                                         h_units = [512, 256, 128], 
                                         weight_decay = [0, 0, 0], dropout_rate = [0, 0, 0], 
                                         num_of_outputs = self.action_space, training_name = training_name)
            
            # update target actor model_names attributes for checkpoints
            self.DDPG_Target_Actor.model_name = "DDPG_Target_Actor"

            # update target actor checkpoints_path attributes
            self.DDPG_Target_Actor.checkpoint_path = os.path.join(self.DDPG_Target_Actor.checkpoint_dir, self.DDPG_Target_Actor.model_name)
            
            # intialise critic model
            self.DDPG_Critic = fc_model(model = "DDPG_Critic",
                                   h_units = [512, 256, 128], 
                                   weight_decay = [0, 0, 0], dropout_rate = [0, 0, 0], num_of_outputs = 1, training_name = training_name)

            # update critic model_names attributes for checkpoints
            self.DDPG_Critic.model_name = "DDPG_Critic"

            # update critic checkpoints_path attributes
            self.DDPG_Critic.checkpoint_path = os.path.join(self.DDPG_Critic.checkpoint_dir, self.DDPG_Critic.model_name)
            
            # intialise target critic model
            self.DDPG_Target_Critic = fc_model(model = "DDPG_Critic",
                                          h_units = [512, 256, 128], 
                                          weight_decay = [0, 0, 0], dropout_rate = [0, 0, 0], num_of_outputs = 1, training_name = training_name)

            # update target critic model_names attributes for checkpoints
            self.DDPG_Target_Critic.model_name = "DDPG_Target_Critic"

            # update target critic checkpoints_path attributes
            self.DDPG_Target_Critic.checkpoint_path = os.path.join(self.DDPG_Target_Critic.checkpoint_dir, 
                                                              self.DDPG_Target_Critic.model_name)
            
            # compile actor, target_actor, critic, target_critic
            self.DDPG_Actor.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = self.lr_actor))
            self.DDPG_Target_Actor.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = self.lr_actor))
            self.DDPG_Critic.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = self.lr_critic))
            self.DDPG_Target_Critic.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = self.lr_critic))
            
            # hard update target models' weights to online network to match initialised weights
            self.update_ddpg_target_models(tau = 1)
            
    def update_ddpg_target_models(self, tau = None): 
        
        """ function to soft update target model weights for DDPG. Hard update is possible if tau = 1 """
        
        # use tau attribute if tau not specified 
        if tau is None:
            
            tau = self.tau
        
        # weight list to store processed target actor weights
        weights = []
        
        # target actor weights
        targets = self.DDPG_Target_Actor.weights
        
        # enumerate over current actors weights
        for i, weight in enumerate(self.DDPG_Actor.weights):
            
            # softcopy of actors weight
            weights.append(weight * tau + targets[i] * (1 - tau))
        
        # append processed weights to target actor 
        self.DDPG_Target_Actor.set_weights(weights)
        
        # weight list to store processed target critic weights
        weights = []
        
        # target critic weights
        targets = self.DDPG_Target_Critic.weights
        
        # enumerate over current critic weights
        for i, weight in enumerate(self.DDPG_Critic.weights):
            
             # softcopy of critic weight
            weights.append(weight * tau + targets[i] * (1 - tau))
        
        # replace processed weights for target critic
        self.DDPG_Target_Critic.set_weights(weights)
        
        
    def store_memory(self, state, action, reward, state_prime, is_done):
    
        """ function to log state, action, state_prime, reward, terminal flag """

            
        self.memory.log(state, action, reward, state_prime, is_done)
        
        
    def select_actions(self, observations, mode):
        
        """ function to select actions for each leg from observations from vicon state """
        """ observations should be a (19,) numpy array """
        
        # list to return actions in numpy 
        actions_list = []
        
        if self.model == "DDPG":
        
            # convert observations into tensor
            state = tf.convert_to_tensor([observations], dtype = tf.float32)
            
            # feed observation tensor to actor model to obtain list of bounded actions (tanh --> +-1)
            actions = self.DDPG_Actor(state)
            
            # increase bound to range of max_action (e.g. +- 10)
            actions = actions * self.max_action

            
            # add gaussian noise if not test
            if mode != "test":
                
                actions += tf.random.normal(shape = [self.action_space], mean = 0.0, stddev = self.noise)
            
            # ensure actions are within range 
            actions = tf.clip_by_value(actions, self.min_action, self.max_action)
            
            # [0] needed as NN outputs in (1,action_space)
            return actions.numpy()[0] 

    def apply_gradients_DDPG(self):
        
        """ function to apply gradients for ddpg """
        """ learns from replay buffer """
        # doesnt not apply gradients if memory does not have at least batch_size number of logs
        if self.memory.mem_counter < self.batch_size:
            return
        
        # randomly sample batch of memory of state, action, state_prime, reward, terminal flag from memory log
        state, action, reward, state_prime, is_done = self.memory.sample_log(self.batch_size)
        
        # convert state, action, state_prime, reward to tensors
        states = tf.convert_to_tensor(state, dtype = tf.float32)
        states_prime = tf.convert_to_tensor(state_prime, dtype = tf.float32)
        actions = tf.convert_to_tensor(action, dtype = tf.float32)
        rewards = tf.convert_to_tensor(reward, dtype = tf.float32)
        
        # record operations for automatic differentiation for critic 
        with tf.GradientTape(persistent = True) as tape: 
            
            # obtain actions from target actor for states_prime
            target_actions = self.DDPG_Target_Actor(states_prime)
            
            # obtain critic q value by feeding critic with states_prime and target_actions 
            target_critic_value = tf.squeeze(self.DDPG_Target_Critic(tf.concat([states_prime, target_actions], axis = 1)), 
                                             axis = 1)
            
            # obtain critic q value by feeding critic with states and actions 
            critic_value = tf.squeeze(self.DDPG_Critic(tf.concat([states, actions], axis = 1)), axis = 1)
            
            # obtain td target
            td_target = rewards + self.discount_rate * target_critic_value * (1 - is_done)
            
            # critic loss is mean squared error between td_target and critic value 
            critic_loss = tf.keras.losses.MSE(td_target, critic_value)
        
        # computes critic gradient for all trainable variables using operations recorded in context of this tape
        critic_gradient = tape.gradient(critic_loss, self.DDPG_Critic.trainable_variables)
        
        # apply critic gradients to all trainable variables in critic model
        self.DDPG_Critic.optimizer.apply_gradients(zip(critic_gradient, self.DDPG_Critic.trainable_variables))
        
        # record operations for automatic differentiation for actor
        with tf.GradientTape(persistent = True) as tape: 
            
            # obtain actions from state following different policy 
            new_pol_actions = self.DDPG_Actor(states)
            
            # gradient ascent using critic value ouput as actor loss
            # loss is coupled with actor model from new_pol_actions 
            actor_loss = -self.DDPG_Critic(tf.concat([states, new_pol_actions], axis = 1))
            
            # reduce mean across batch_size
            actor_loss = tf.math.reduce_mean(actor_loss)
        
        # computes actor gradient for all trainable variables using operations recorded in context of this tape
        actor_gradient = tape.gradient(actor_loss, self.DDPG_Actor.trainable_variables)
        
        # apply actor gradients to all trainable variables in actor model
        self.DDPG_Actor.optimizer.apply_gradients(zip(actor_gradient, self.DDPG_Actor.trainable_variables))        

        # increment of apply_grad_counter
        self.apply_grad_counter += 1 

        # SOFT COPY OPTION: update target models based on user specified tau
        if self.update_target == None:

             self.update_ddpg_target_models()    

        # HARD COPY OPTION EVERY update_target steps
        else:
            if self.apply_grad_counter % self.update_target == 0: 
            
                self.update_ddpg_target_models(tau = 1)

        # gather total loss for logging
        total_loss = critic_loss + actor_loss

        # return the total loss for logging
        return total_loss.numpy()

    def save_all_models(self):
        
        """ save weights for all models """
        
        print("saving model!")
        # for ddpg 
        if self.model == "DDPG":
            
            # save weights for each actor, target_actor, critic, target_critic model
            self.DDPG_Actor.save_weights(self.DDPG_Actor.checkpoint_path)
            self.DDPG_Target_Actor.save_weights(self.DDPG_Target_Actor.checkpoint_path)
            self.DDPG_Critic.save_weights(self.DDPG_Critic.checkpoint_path)
            self.DDPG_Target_Critic.save_weights(self.DDPG_Target_Critic.checkpoint_path)
        

    def load_all_models(self):
        
        """ load weights for all models """
        
        print("loading model!")
        if self.model == "DDPG":
            
            # load weights for each actor, target_actor, critic, target_critic model
            self.DDPG_Actor.load_weights(self.DDPG_Actor.checkpoint_path).expect_partial()
            self.DDPG_Target_Actor.load_weights(self.DDPG_Target_Actor.checkpoint_path).expect_partial()
            self.DDPG_Critic.load_weights(self.DDPG_Critic.checkpoint_path).expect_partial()
            self.DDPG_Target_Critic.load_weights(self.DDPG_Target_Critic.checkpoint_path).expect_partial()


