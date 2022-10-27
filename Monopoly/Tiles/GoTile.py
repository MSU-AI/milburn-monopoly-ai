
from Tiles.Tile import Tile

class GoTile(Tile):
    """
    Represents the "GO" tile on the board.
    """
<<<<<<< HEAD

    def __init__(self, name, player, balance : int):
=======
    #THIS TILE DOES NOT HAVE AN OWNER
    def __init__(self):
>>>>>>> 20851e5157d482de3b8cdaf049e45caf0fc99d0d
        """
        Initializes the "GO" tile.
        """
        super().__init__()
        self.name = "GO"
        self.player = player
        self.balance = balance  
    def GO(self, balance):
        self.balance = balance + 200
        return self.balance
