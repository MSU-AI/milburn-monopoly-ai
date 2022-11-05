import pygame
from Tiles.Tile import Tile

class JailTile(Tile):
    """
    Represents the "Jail" tile on the board.
    """
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self, attributes):
        """
        Initializes the "Jail" tile.
        """
        
        self.color = 'Brown'
        self.name = 'Jail'
        self.type = attributes['Space']
        self.owner = "Bank"
        super().__init__()