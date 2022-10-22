
from Tile import Tile

class ParkingTile(Tile):
    """
    Represents the "Free Parking" tile on the board.
    """

    def __init__(self, name):
        """
        Initializes the "Free Parking" tile.
        """
        super().__init__()
        self.name = "Free Parking"

