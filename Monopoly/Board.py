
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

        # TODO: Save any specific tile attributes (property, jail, go, etc.)
        #       Will want to store the CSV data here somehow.
        
        self.players = set()  # Set of players currently on tile

class Board:
    """
    Represents the Monopoly game board.
    """
    
    WIDTH, HEIGHT = 750, 750  # Board size
    COLOR = (191, 219, 174)  # Board color
    LENGTH = 10  # The number of tiles on one side of the board.
    SIDES = 4  # The number of sides on the board.

    def __init__(self, window):
        """
        Initializes the game board.
        """
        self.window = window

        # Initializes board as a list of the board's sides and tiles.
        self.board = [
            [ Tile() for i in range(self.LENGTH) ] for j in range(self.SIDES)
        ]

    def draw(self):
        """
        Draws the game board. 
        """
        self.window.fill(self.COLOR)

        # TODO: Draw individual tiles here, preferably similar to an actual
        #       Monopoly board (as rectangles around the perimeter).
        #       Hint: Take a look at pygame.draw.rect()!
