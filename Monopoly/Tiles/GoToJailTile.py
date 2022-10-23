
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
