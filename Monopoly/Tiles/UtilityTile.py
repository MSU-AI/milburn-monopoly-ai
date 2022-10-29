from Tiles.Tile import Tile
from Player import Player
from Board import Board
class UtilityTile(Tile):
    """
    Represents a utility tile on the board.
    """
    
    def __init__(self, attributes: dict):
        """
        Initializes the utility tile.
        """
        super().__init__()
        self.space = attributes['Space']
        self.name = attributes['Name']
        self.owner = "Bank"
        self.price = attributes['Price']
        self.mortgage_value = self.price/2
        self.is_mortgaged = False
        #self.position = attributes['Position(X)', 'Position(Y)']
        self.position = [attributes['Position(X)'], attributes['Position(Y)']]
    
    #sets ownwer to player
    def setOwner(self, player):
        self.owner = player
    
    #Returns the rent for the property. If player is the owner nothing happens, if the property is mortgaged nothing happens, 
    #if it is owned by the bank nothing happens, if the property is not mortgaged and the player is not the owner the rent is returned.
    #Look at Game.py for compareUtilities function
    def getRent(self):
        if self.owner.properties[1][2]:
            if self.owner.properties[2][8]:
                return 10 * self.owner.movecount
            else:
                return 4 * self.owner.movecount

    #Morgages the property. Returns the mortgage value.
    def mortgage(self):
        self.is_mortgaged = True
        self.owner.mortgage(self)
        return self.mortgage_value

    #Unmortgages the property. Returns the amount owed to bank value.
    def unMortgage(self):
        self.is_mortgaged = False
        return self.mortgage_value * 1.1
