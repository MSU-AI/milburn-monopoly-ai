import numpy as np
from Tile import Tile
from Player import Player
from JailTile import JailTile

class ChanceTile(Tile):
    """
    Represents a "Chance" tile on the board.
    """

    def __init__(self, attributes: dict):
        """
        Initializes the "Chance" tile.
        """
        self.deck = []
        self.players = np.array([])
        super().__init__()        
        
        
    def goToGo(player):
        player.pos = np.array([0,0])
        player.getMoney(200)
    
    
    def goIllinoisAve(player):
        #need to check players current position to see if they pass go
        if (player.pos == [0,7]):
            player.pos = np.array([2,4])
        
        elif (player.pos == [2,2]):
            player.pos = np.array([2,4])
        
        elif (player.pos == [3,6])
            player.pos = np.array([2,4])
            player.getMoney(200)


    def goCharlesPlace(self, player):
        #need to check players current position to see if they pass go
        if (player.pos == [0,7]):
            player.pos = np.array([1,1])
        
        elif (player.pos == [2,2]):
            player.pos = np.array([1,1])
            player.getMoney(200)
            
        
        elif (player.pos == [3,6])
            player.pos = np.array([1,1])
            player.getMoney(200)


    def goNearestUtility(self, player):
        #need to check players current position to find closest ulitily
        if (player.pos == [0,7]):
            player.pos = np.array([1,2])
        
        elif (player.pos == [2,2]):
            player.pos = np.array([2,8])
        
        elif (player.pos == [3,6])
            player.pos = np.array([1,2])    
    
    
    def goNearestRailRoad(player):
        #need to check players current position to find closest railroad
        if (player.pos == [0,7]):
            player.pos = np.array([1,5])
        
        elif (player.pos == [2,2]):
            player.pos = np.array([2,5])
        
        elif (player.pos == [3,6])
            player.pos = np.array([0,5])      
    
    def bankDividends(player):
        player.addMoney(200)
        
    
    def getOutOfJail(player):
        player.addGetOutOfJail()
        
        
    def goToJail(player):
        player.updatePos([1,0])
        
        
    def goBackThree(player):
        #need to check players current position to see which tile they go back to
        if (player.pos == [0,7]):
            player.pos = np.array([0,4])
        
        elif (player.pos == [2,2]):
            player.pos = np.array([1,9])
        
        elif (player.pos == [3,6])
            player.pos = np.array([3,3])
    
    def generalRepairs(player):
        player.payTax(price = player.houses * 25 + player.hotels * 100)
        
        
    def poorTax(player):
        player.payTax(price = 15)
        
        
    def goReadingRailroad(player):
        player.pos = np.array([0,5])
        
        
    def goBoardwalk(player):
        player.pos = np.array([3,9])
        
    def boardChairman(player, players):
        for payer in players:
            if(payer != player):
                player.payTax(payer, 50)
                
                
    def buildingLoan(player):
        player.addMoney(150)
        
        
    def crosswordWin(player):
        player.addMoney(100)
        
