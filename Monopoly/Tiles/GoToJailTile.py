import pygame
from Tiles.Tile import Tile

class GoToJailTile(Tile):
    """
    Represents the "Go to Jail" tile on the board.
    """
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self):
        """
        Initializes the "Go to Jail" tile.
        """
        super().__init__()
        self.color = 'Red'
    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS[self.color],
            (x, y, self.WIDTH, self.HEIGHT)
        )
