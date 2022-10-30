import pygame
from Tiles.Tile import Tile

class JailTile(Tile):
    """
    Represents the "Jail" tile on the board.
    """
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self):
        """
        Initializes the "Jail" tile.
        """
        super().__init__()
        self.color = 'Brown'
        self.name = 'Jail'
    