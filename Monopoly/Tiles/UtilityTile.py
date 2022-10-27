
from Tiles.Tile import Tile

class UtilityTile(Tile):
    """
    Represents a utility tile on the board.
    """
    
    def __init__(self, name, position, owner):
        """
        Initializes the utility tile.
        """
        super().__init__()
        self.type = 'utility'
        self.name = name
        self.owner = owner
        self.price = 150
        self.mortgage_value = 75
        self.is_mortgaged = False
        self.position = position
    
    #sets ownwer to player
    def setOwner(self, Player):
        self.owner = Player
    
    #Returns the rent for the property. If player is the owner nothing happens, if the property is mortgaged nothing happens, 
    #if it is owned by the bank nothing happens, if the property is not mortgaged and the player is not the owner the rent is returned.
    def getRent(self, balance, charge):
        balance = balance - charge 
        # need to figure out how to find out if player also owns another utility tile and then multiply the dice roll by 10

    #Morgages the property. Returns the mortgage value.
    def mortgage(self):
        self.is_mortgaged = True
        return self.mortgage_value

    #Unmortgages the property. Returns the amount owed to bank value.
    def unMortgage(self):
        self.is_mortgaged = False
        return self.mortgage_value * 1.1
