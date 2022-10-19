import pandas as pd
import pygame
def readCSV():
    df = pd.read_csv('Data/newboard.csv', delimiter=',')
    return df
# TODO: CREATE A FUNCTION THAT INITIALIZES ALL THE PROPERTIES
# CHECK OUT THE IPYNB IN THE ROOT DIRECOTRY TO SEE HOW THE DATA FRAME LOOKS, YOU PROBABLY WANT TO SEPARATE CREATION OF OBJECTS DEPENDING ON IS IT A STREET,
# UTILITY OR RAIL ROAD
# QUICK REMAINDER, COLUMN IN THE DATA FRAME RentBuild5 MEANS RENT WHEN HOTEL IS BUILT, THINK OF A WAY TO IMPLEMENT THAT,
# MY SUGGESTION WOULD BE AN ARRAY OF PRICES AS ATTRIBUTE AND DEPENDING ON NUM OF BUILDS RETRIEVE CORRESPONDING VALUE
# FOR EXAMPLE: BALTIC AVENUE -> RENTS[4,20,60,180,320,450] , BUILD = 3, RENT = RENTS[BUILD]
def initProperty(df):
    pass

class Tile:
    """
    Represents a tile on the board.
    """

    WIDTH, HEIGHT = 40, 40  # Tile size

    def __init__(self):
        """
        Initializes a Tile object.
        """

        # TODO: Save any property attributes.
        # TODO: Save which player(s) are on the current tile (if any).

class Board:
    """
    Represents the Monopoly game board.
    """
    
    WIDTH, HEIGHT = 500, 500  # Board size

    LENGTH = 10  # The number of tiles on one side of the board.
    SIDES = 4  # The number of sides on the board.

    def __init__(self, window):
        """
        Initializes the game board.
        """
        self.window = window
        self.board = [Tile() for _ in range(self.LENGTH * self.SIDES)]

    def draw(self):
        """
        Draws the game board. 
        """
        
        # TODO: Draw game board.
