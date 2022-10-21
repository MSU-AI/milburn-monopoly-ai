
import pygame

class Tile:
    """
    Represents a tile on the board.
    """

    COLORS = {
        'black' : (0, 0, 0)
    }
    WIDTH, HEIGHT = 70, 70  # Tile size

    def __init__(self, name=""):
        """
        Initializes the tile.
        """
        self.name = name

    def draw(self, window, x, y):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS['black'],
            (x, y, self.WIDTH, self.HEIGHT)
        )
