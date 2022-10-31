import torch
import random
import numpy as np
from collections import deque
from Game import Game
from Model import QNet, QTrainer

learning_rate = 0.001
class Agent:
    def __init__(self, players):
        self.players = self.player
        self.games = 0
        self.epsilon = 0 
        self.gamma = 0.8
        self.memory = deque(maxlen=1_000_000)
        self.model = QNet(3, 256, 1)
        self.trainer = QTrainer(self.model, lr = learning_rate, gamma = self.gamma)
    
    def getState(self):
        pass 