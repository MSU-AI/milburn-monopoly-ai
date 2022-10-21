
from Tiles.Tile import Tile

import pygame

pygame.font.init()

# import pandas as pd

# def readCSV():
#     df = pd.read_csv('Data/newboard.csv', delimiter=',')
#     return df

# # TODO: CREATE A FUNCTION THAT INITIALIZES ALL THE PROPERTIES
# # CHECK OUT THE IPYNB IN THE ROOT DIRECOTRY TO SEE HOW THE DATA FRAME LOOKS, YOU PROBABLY WANT TO SEPARATE CREATION OF OBJECTS DEPENDING ON IS IT A STREET,
# # UTILITY OR RAIL ROAD
# # QUICK REMAINDER, COLUMN IN THE DATA FRAME RentBuild5 MEANS RENT WHEN HOTEL IS BUILT, THINK OF A WAY TO IMPLEMENT THAT,
# # MY SUGGESTION WOULD BE AN ARRAY OF PRICES AS ATTRIBUTE AND DEPENDING ON NUM OF BUILDS RETRIEVE CORRESPONDING VALUE
# # FOR EXAMPLE: BALTIC AVENUE -> RENTS[4,20,60,180,320,450] , BUILD = 3, RENT = RENTS[BUILD]

# def initProperty(df):
#     pass

class Board:
    """
    Represents the Monopoly game board.
    """
    
    COLORS = {
        'board' : (219, 219, 219),
        'black' : (0, 0, 0)
    }
    FONT = pygame.font.SysFont(pygame.font.get_fonts()[73], 100)  # Title font

    def __init__(self):
        """
        Initializes the game board.
        """
        # Initializes board as a list of the board's sides and tiles.
        self.board = [ [ Tile() for i in range(10) ] for j in range(4) ]

    def draw(self, window, pad):
        """
        Draws the game board. 
        """
        # Fills screen with background color, wiping the screen of artifacts
        window.fill(self.COLORS['board'])

        # Renders title header
        title = self.FONT.render( "monopoly", 1, self.COLORS['black'] )
        window.blit( title, (
            window.get_width() / 2 - title.get_width() / 2,
            window.get_height() / 2 - title.get_height() / 2
        ))

        # TODO: Currently drawing default Tiles; once all Tiles have been
        #       implemented, that can be changed to draw the correct tiles!

        # Draw board tiles
        for s, side in enumerate(self.board):
            for t, tile in enumerate(side):

                # TODO: Math here is super janky; probably could be simplified.

                # Tiles are drawn on their side accordingly
                if s == 0:
                    tile.draw(
                        window,
                        t * tile.WIDTH + pad,
                        pad
                    )
                elif s == 1:
                    tile.draw(
                        window,
                        window.get_width() - pad * 2 - tile.WIDTH + pad,
                        t * tile.HEIGHT + pad
                    )
                elif s == 2:
                    tile.draw(
                        window,
                        window.get_width() - pad * 2 - tile.WIDTH + pad - t * tile.WIDTH,
                        window.get_height() - pad * 2 - tile.HEIGHT + pad
                    )
                elif s == 3:
                    tile.draw(
                        window,
                        pad,
                        window.get_height() - pad - (t + 1) * tile.HEIGHT
                    )
