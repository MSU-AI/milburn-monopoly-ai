
import pygame

class Tile:
    """
    Represents a tile on the board.
    """

    COLORS = {
        'Black' : (0, 0, 0),
        'Brown' : (102, 51, 0),
        'LightBlue' : (102, 178, 255),
        'Pink' : (255, 153, 204),
        'Orange' : (255, 128, 0),
        'Red' : (255, 0, 0),
        'Yellow' : (255, 255, 51),
        'Green' : (0, 255, 0),
        'Blue' : (0, 128, 255)
    }
    WIDTH, HEIGHT = 70, 70  # Tile size

    def __init__(self, name: str = "tile_name"):
        """
        Initializes the tile.
        """
        self.name = name

    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS['Black'],
            (x, y, self.WIDTH, self.HEIGHT)
        )
