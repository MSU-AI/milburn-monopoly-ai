from multiprocessing.spawn import import_main_path
import pygame
from enum import Enum
import random

#Create all the classes 

#initializes the game
pygame.init()

#TO DO: reset

#TO DO: reward

#TO DO: play(pos, property, money and etc...)  and it makes a decision (buy, sell, auction, 
# pass(although that triggers an auction if on un owned tile)) 

#TO DO: turns
#TO DO: DETERMINE keybinds for actions that will be used both by model and us when we decide to play against it
#TO DO: create very simple but usable visuals for the game(2D) 
class MonopolyBoard:
    #TO DO: finish the initialization
    def __init__(self) -> None:
        pass
    #TO DO: finish this function 
    def turn(self):
        pass
    def roll_dice():
        pass

if __name__ == '__main__':
    game = MonopolyBoard()
    while True:
        game_over, scoreboard = game.turn()

        if game_over == True:
            break

pygame.quit()