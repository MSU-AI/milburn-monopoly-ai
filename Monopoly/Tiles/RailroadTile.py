from Tiles.Tile import Tile

import pygame


class RailroadTile(Tile):
    """
    Represents a railroad tile on the board.
    """
    
    def __init__(self, attributes: dict, bank):
        """
        Initializes the railroad tile.
        """
        
        self.Name = attributes["Name"]
        self.Position_X = attributes["Position(X)"]
        self.Position_Y = attributes["Position(Y)"]
        self.Rent = attributes["Rent"]
        self.Mortgage = False 
        
        self.owner = bank
        self.trainstation_count = 0
        super().__init__()
      
    def calcRent(self):
        #Rent when player lands on Train Station Tile
        #Each Railroad costs a base price of $200
        #Rent is contingent upon how many railroads that player owns
        #$25 for one; $50 for two, $100 for three; $200 for four
        if self.owner == Bank:
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
       return 100
   
    def unMortgage(self):
       self.mortage = False
    
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
