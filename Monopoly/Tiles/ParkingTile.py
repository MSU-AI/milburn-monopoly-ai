
from Tiles.Tile import Tile

class ParkingTile(Tile):
    """
    Represents the "Free Parking" tile on the board.
    """
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self):
        """
        Initializes the "Free Parking" tile.
        """
        super().__init__()
