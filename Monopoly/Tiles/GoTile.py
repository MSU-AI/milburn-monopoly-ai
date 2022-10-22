
from Tile import Tile

class GoTile(Tile):
    """
    Represents the "GO" tile on the board.
    """

    def __init__(self, name, player, balance : int):
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
