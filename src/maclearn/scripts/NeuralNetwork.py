""" 
Neural Network model classes using TensorFlow 2.3.1
Purpose : efficiently generate model architecture by building from subclasses
5 Algorithm networks available: MAD3QN, MAA2C, A2CMA, A2CSA, DDPG 
"""

# Standard Import
import tensorflow as tf

class fc_block(tf.keras.layers.Layer):
    
    def __init__(self, h_units, weight_decay, dropout_rate):
        
        """ class constructor that creates the layers attributes for fc_block """
        
        # inherit class constructor attributes from tf.keras.layers.Layer
        super(fc_block, self).__init__()
        
        # add dense layer attribute with L2 Regulariser
        self.dense = tf.keras.layers.Dense(h_units, use_bias = False, kernel_regularizer = 
                                            tf.keras.regularizers.l2(l = weight_decay))
        
        # add batch norm layer attribute
        self.batch_norm = tf.keras.layers.BatchNormalization()
    
    def call(self, inputs, training = False):
        
        """ function for forward pass of model """
        """ includes training argument as batch_norm functions differently during training and during inference """
        
        # inputs --> dense --> relu --> batch_norm --> output
        x = self.dense(inputs)
        x = tf.nn.relu(x)
        x = self.batch_norm(x, training = training)

        return x

class fc_model(tf.keras.Model):
    
    def __init__(self, model, h_units, weight_decay, dropout_rate, num_of_outputs, training_name):
        
        """ class constructor that creates the layers attributes for fully connected model """
        
        # inherit class constructor attributes from tf.keras.Model
        super(fc_model, self).__init__()
        
        # model name
        self.model_name = None
        
        # type of model architecture
        self.model = model
         
        # checkpoint directory
        self.checkpoint_dir = "Saved_Models/" + training_name + "_" + "best_models/"
        
        # checkpoint filepath 
        self.checkpoint_path = None
        
        # create intended number of dqn_block attributes
        self.block_1 = fc_block(h_units[0], weight_decay[0], dropout_rate[0])
        self.block_2 = fc_block(h_units[1], weight_decay[1], dropout_rate[1])
        self.block_3 = fc_block(h_units[2], weight_decay[2], dropout_rate[2])
            
        # create final output layer attribute        
        if self.model == "DDPG_Actor":
            
            # output layer with continuous action for each joint
            self.outputs = tf.keras.layers.Dense(num_of_outputs, activation = 'tanh')
        
        elif self.model == "DDPG_Critic": 

            # output layer is state-action value, Q, for a given state and action
            self.outputs = tf.keras.layers.Dense(num_of_outputs)
                     
    def call(self, inputs, training = False):
        
        """ function for forward pass of model """
        """ includes training argument as batch_norm functions differently during training and during inference """
            
        # input --> block_1 --> block_2 --> block_3 
        x = self.block_1(inputs, training = training)
        x = self.block_2(x, training = training)
        x = self.block_3(x, training = training)

        # output for MAA2C or DDPG  
        # block_3 --> outputs 
        x = self.outputs(x)

        return x
