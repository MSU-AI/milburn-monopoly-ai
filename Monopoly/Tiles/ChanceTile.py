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
        #only get 200 if they pass go
        player.pos = np.array([2,4])
        player.getMoney(200)

    def goCharlesPlace(player):
        #only get 200 if they pass go
        player.pos = np.array([1,1])
        player.getMoney(200)

    def goNearestUtility(player):
        pass
    
    def goNearestRailRoad(player):
        pass
    
    def bankDividends(player):
        player.addMoney(200)
    
    def getOutOfJail(player):
        player.addGetOutOfJail()
        
    def goToJail(player):
        player.updatePos([1,0])
        
    def goBackThree(player):
        pass
    
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
