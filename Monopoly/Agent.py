import torch
import os
import numpy as np
import random
from collections import deque
from Model import QNet, QTrainer
from Player import Player
from RL.Action import Action
MAX_MEMORY = 100_000
learning_rate = 0.001
class Agent(Player):
    def __init__(self, board, bank):
        self.epoch = 0
        self.games = 0
        self.model = QNet(4, 150, 3)
        self.trainer = QTrainer(self.model, learning_rate, 0.9)
        self.memory = deque(maxlen=1000000)
    """
    Creates a state that describes the env around our agent.
    The size of the state determines the size of the input layer for the QNet(first argument)

    """
    def getState(self, player, board):
        tile = board[player.position[0]][player.position[1]]
        #IMPORTANT IF STATE SIZE IS N THEN QNET INPUT MUST BE N
        # TODO: Create a better state
        # TODO: Use pruning in the future to find the optimal state(Do not worry about it for now)
        state = [player.worth, player.position[0], player.position[1], tile.group]
        
        return np.array(state, dtype = int)
    """
    Gets actions based on either randomly picking an action or from model predictions
    When self.epsilon = 0, only makes decisions based on model
    [1,0,0] -> Spend Money (buy tile, buy house/hotel)
    [0,1,0] -> Get money(sell house/hotel, mortgage property)
    [0,0,1] -> Do nothing
    You get the action array in this form by extracting the index of max value tensor returned
    by model prediction, and use it to set the same index to one and rest zeros
    """
    def getAction(self, state):
        self.epsilon = 100 - self.games
        final_action = [0,0,0]
        if random.randint(0, 240) < self.epsilon:
            move = random.randint(0,2)
            final_action[move] = 1
        else:
            state0 = torch.tensor(state, dtype = torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_action[move] = 1
        return final_action
    """
    Records state, action, reward, next state and done(True if game over/False otherwise)
    """
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
    """
    Trains by going over the memory and making choices based on the current model
    """
    def trainLongMemory(self):
        if len(self.memory) > 1000:
            mini_sample = random.sample(self.memory, 1000)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)
    
            


        