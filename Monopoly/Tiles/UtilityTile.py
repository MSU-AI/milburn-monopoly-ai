
from Tile import Tile
from Bank import Bank
from Player import Player


#Electric Company / Water Works
#price = 150
#diceroll * 4 if one utility owned or 10 if both owned
#code for the Electric Company and Water Works

class UtilityTile(Tile):
    """
    Represents a utility tile on the board.
    """
    
    def __init__(self, name, position):
        """
        Initializes the utility tile.
        """
        self.type = 'utility'
        self.name = name
        self.owner = Bank
        self.price = 150
        self.mortgage_value = 75
        self.is_mortgaged = False
        self.position = position
        self.house_count = 0
        self.hotel_count = 0
        super().__init__()
    
    #sets ownwer to player
    def setOwner(self, Player):
        self.owner = Player
    
    #Returns the rent for the property. If player is the owner nothing happens, if the property is mortgaged nothing happens, 
    #if it is owned by the bank nothing happens, if the property is not mortgaged and the player is not the owner the rent is returned.
    def getRent(self, diceroll):
        if self.is_mortgaged == True or self.owner == Bank:
            return 0
        elif self.owner == Player:
            return diceroll * 4
        else:
            return diceroll * 10
        # need to figure out how to find out if player also owns another utility tile and then multiply the dice roll by 10

    #Morgages the property. Returns the mortgage value.
    def mortgage(self):
        self.is_mortgaged = True
        return self.mortgage_value

    #Unmortgages the property. Returns the amount owed to bank value.
    def unMortgage(self):
        self.is_mortgaged = False
        return self.mortgage_value * 1.1
