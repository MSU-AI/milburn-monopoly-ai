from Tiles.Tile import Tile
from Player import Player
class GoTile(Tile, Player):
    """
    Represents the "GO" tile on the board.
    """

    def __init__(self, attributes: dict, init_players):
        """
        Initializes the "GO" tile.
        """
        super().__init__()
        self.name = attributes['Name']
        self.position = [attributes['Position(X)'],attributes['Position(Y)']]
        self.color = 'Black'
        self.players_on_tile = 0

    def GO(self):
        self.balance = self.balance + 200
        return self.balance