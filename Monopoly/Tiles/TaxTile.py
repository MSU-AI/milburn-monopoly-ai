from Tiles.Tile import Tile

class TaxTile(Tile):
    """
    Represents a tax tile on the board.
    """

    def __init__(self, attributes: dict):
        """
        Initializes the tax tile.
        """
        self.owner = 'IRS'
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
        
    def incomeTax(self):
        #if player lands on Income Tax tile
        return 200

    def luxuryTax(self):
        #if player lands on the Luxury Tax tile
        return 75
