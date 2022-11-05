from Tiles.Tile import Tile

class RailroadTile(Tile):
    """
    Represents a railroad tile on the board.
    """
    
    def __init__(self, attributes: dict, bank):
        """
        Initializes the railroad tile.
        """

        

        
        self.name = attributes["Name"]
        self.space = attributes['Space']
        self.price = attributes['Price']
        self.position = [attributes['Position(X)'], attributes['Position(Y)']]  
        self.rent = attributes["Rent"]
        self.mortgage_value = self.price/2
        self.is_mortgaged = False
        self.owner = bank
        self.bank = bank
        self.color = 'Red'
        self.type = attributes['Space']
        super().__init__()
        self.trainstation_count = 0
      
    def calcRent(self):
        #Rent when player lands on Train Station Tile
        #Each Railroad costs a base price of $200
        #Rent is contingent upon how many railroads that player owns
        #$25 for one; $50 for two, $100 for three; $200 for four
        if self.owner == self.bank:
            return 0
        elif self.trainstation_count == 0:
            return 25
        elif self.trainstation_count == 1:
            return 50
        elif self.trainstation_count == 2:
            return 100
        elif self.trainstation_count == 4:
            return 200
        else:
            return 0
   
    def mortgage(self):
       self.mortgage = True
       return self.mortgage_value
   
    def unMortgage(self):

       self.mortgage = False
       return self.mortgage_value * 1.1

    
    def buyTrainStation(self):
        #Purchase Train Station Tile
        if self.trainstation_count >= 0 and self.trainstation_count <= 3:
            self.trainstation_count += 1
        
    
    def sellTrainStation(self):
        #Sells Train Station Property
        if self.trainstation_count >= 1 and self.trainstation_count <= 4:
            self.trainstation_count -= 1
    
    def setOwner(self, Player):
        #Applies ownership of Train Station Property to player
        self.owner = Player
    def Bankruptcy(self, bank):
        
        self.setOwner(bank)
    def getMortVal(self):
        return self.mortgage_value 
        
