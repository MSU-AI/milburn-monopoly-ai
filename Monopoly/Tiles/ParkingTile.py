from Tiles.Tile import Tile
import pygame

class ParkingTile(Tile):
    """
    Represents the "Free Parking" tile on the board.
    """

    def __init__(self, attributes : dict):
        """
        Initializes the "Free Parking" tile.
        """
        
        self.name = attributes['Name']
        self.position = [attributes['Position(X)'], attributes['Position(Y)']]
        self.color  = 'BabyBlue'
        self.type = attributes['Space']
        self.owner = "Bank"
        super().__init__()
    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS[self.color],
            (x, y, self.WIDTH, self.HEIGHT)
        )