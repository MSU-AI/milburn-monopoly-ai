
from Tiles.Tile import Tile
from Tiles.GoTile import GoTile
from Tiles.StreetTile import StreetTile
from Tiles.ChestTile import ChestTile
from Tiles.TaxTile import TaxTile
from Tiles.RailroadTile import RailroadTile
from Tiles.ChanceTile import ChanceTile
from Tiles.JailTile import JailTile
from Tiles.UtilityTile import UtilityTile
from Tiles.ParkingTile import ParkingTile
from Tiles.GoToJailTile import GoToJailTile

import pandas as pd
import pygame

pygame.font.init()

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
        self.board = self.make_board()

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

    def make_board(self):
        """
        Reads board information from CSV file.
        """
        data = pd.read_csv('Monopoly/Data/newboard.csv')
        board = [ [], [], [], [] ]

        for index, row in data.iterrows():
            side = index // 10
            attributes = dict(row)

            # TODO: Currently uses default (empty) Tile constructors; should be
            #       changed to take attributes as an argument (see line 110).

            if row['Space'] == "Go":
                board[side].append( GoTile() )
            elif row['Space'] == "Street":
                board[side].append( StreetTile(attributes) )
            elif row['Space'] == "Chest":
                board[side].append( ChestTile() )
            elif row['Space'] == "Tax":
                board[side].append( TaxTile() )
            elif row['Space'] == "Railroad":
                board[side].append( RailroadTile() )
            elif row['Space'] == "Chance":
                board[side].append( ChanceTile() )
            elif row['Space'] == "Jail":
                board[side].append( JailTile() )
            elif row['Space'] == "Utility":
                board[side].append( UtilityTile() )
            elif row['Space'] == "Parking":
                board[side].append( ParkingTile() )
            elif row['Space'] == "GoToJail":
                board[side].append( GoToJailTile() )
            else:
                raise KeyError(f"Invalid tile type in CSV: {row['Space']}")
        
        return board
