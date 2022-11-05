from Tiles.Tile import Tile
class UtilityTile(Tile):
    """
    Represents a utility tile on the board.
    """
    
    def __init__(self, attributes: dict, bank):
        """
        Initializes the utility tile.
        """
        
        self.type = attributes['Space']
        self.name = attributes['Name']
        self.owner = bank
        self.price = attributes['Price']
        self.mortgage_value = self.price/2
        self.is_mortgaged = False
        #self.position = attributes['Position(X)', 'Position(Y)']
        self.position = [attributes['Position(X)'], attributes['Position(Y)']]
        self.color = 'DarkGreen'
        super().__init__()
    
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
    def calcRent(self):
        #electric = self.board[1][2]
        #water = self.board[2][8]
        #if electric.owner == water.owner:
          #  currentTile.getRent(player,diceroll * 10)
        #else:
         #   currentTile.getRent(player,diceroll * 4)
        return 50
    def Bankruptcy(self, bank):
        
        self.setOwner(bank)
    def getMortVal(self):
        return self.mortgage_value
