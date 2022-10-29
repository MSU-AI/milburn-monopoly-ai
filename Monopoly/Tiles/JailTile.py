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
    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS[self.color],
            (x, y, self.WIDTH, self.HEIGHT)
        )
