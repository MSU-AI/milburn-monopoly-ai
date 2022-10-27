
from Tiles.Tile import Tile

class ParkingTile(Tile):
    """
    Represents the "Free Parking" tile on the board.
    """
<<<<<<< HEAD

    def __init__(self, name):
=======
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self):
>>>>>>> 20851e5157d482de3b8cdaf049e45caf0fc99d0d
        """
        Initializes the "Free Parking" tile.
        """
        super().__init__()
        self.name = "Free Parking"

