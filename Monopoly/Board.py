
import pygame

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
