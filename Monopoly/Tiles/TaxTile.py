
from Tile import Tile

class TaxTile(Tile):
    """
    Represents a tax tile on the board.
    """

    def __init__(self):
        """
        Initializes the tax tile.
        """
        self.owner = 'IRS'
        super().__init__()
