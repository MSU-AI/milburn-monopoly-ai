import pygame
from Tiles.Tile import Tile

class GoToJailTile(Tile):
    """
    Represents the "Go to Jail" tile on the board.
    """
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self,attributes):
        """
        Initializes the "Go to Jail" tile.
        """
        
        self.color = 'Red'
        self.name  = 'Go To Jail'
        self.type = attributes['Space']
        self.owner = "Bank"
        super().__init__()
        
