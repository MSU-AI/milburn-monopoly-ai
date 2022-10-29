from Tiles.Tile import Tile

class ParkingTile(Tile):
    """
    Represents the "Free Parking" tile on the board.
    """

    def __init__(self, attributes : dict):
        """
        Initializes the "Free Parking" tile.
        """
        super().__init__()
        self.name = attributes['Name']
        self.position = attributes['Position(X)', 'Position(Y)']