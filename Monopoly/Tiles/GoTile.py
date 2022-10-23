
from Tile import Tile

class GoTile(Tile):
    """
    Represents the "GO" tile on the board.
    """
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self):
        """
        Initializes the "GO" tile.
        """
        super().__init__()
