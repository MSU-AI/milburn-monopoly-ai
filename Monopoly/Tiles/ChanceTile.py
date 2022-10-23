from Tile import Tile
from Bank import Bank
from Player import Player

class ChanceTile(Tile):
    """
    Represents a "Chance" tile on the board.
    """

    def __init__(self, attributes: dict):
        """
        Initializes the "Chance" tile.
        """
        super().__init__()
        
    def drawCard(self):
        #where a random card will be draw by the player
        #unsure of how to draw random chance card
        #unsure of how to implement actions of random chance card
        #https://github.com/LiYChristopher/cli-monopoly/blob/master/cards.csv 
        #above link cotains a csv of the community chest and chance cards
        pass
