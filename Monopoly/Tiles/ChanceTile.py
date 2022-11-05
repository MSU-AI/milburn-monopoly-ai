
from Tiles.Tile import Tile
import pygame




class ChanceTile(Tile):
    """
    Represents a "Chance" tile on the board.
    """

    def __init__(self, attributes: dict):
        """
        Initializes the "Chance" tile.
        """

        
        self.color = 'Blue'
        self.name = '?'
        self.type = attributes['Space']
        self.owner = "Bank"
        super().__init__()
        
  
        self.deck = []
        self.players = np.array([])
        super().__init__()        
        
        
    def goToGo(player):
        player.pos = np.array([0,0])
        player.getMoney(200)
    
    
    def goIllinoisAve(player):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = np.array([2,4])
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = np.array([2,4])
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = np.array([2,4])
            player.getMoney(200)


    def goCharlesPlace(self, player):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = np.array([1,1])
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = np.array([1,1])
            player.getMoney(200)
            
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = np.array([1,1])
            player.getMoney(200)


    def goNearestUtility(self, player):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = np.array([1,2])
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = np.array([2,8])
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = np.array([1,2])    
    
    
    def goNearestRailRoad(player):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = np.array([1,5])
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = np.array([2,5])
        
        elif (player.position[0] == 3 and player.position[1] == 6):
            player.pos = np.array([0,5])      
    
    def bankDividends(player):
        player.addMoney(200)
        
    
    def getOutOfJail(player):
        player.addGetOutOfJail()
        
        
    def goToJail(player):
        player.updatePos([1,0])
        
        
    def goBackThree(player):
        if (player.position[0] == 0 and player.position[1] == 7):
            player.pos = np.array([0,4])
        
        elif (player.position[0] == 2 and player.position[1] == 2):
            player.pos = np.array([1,9])
        
        elif (player.position[0] == 3 and player.position[1] == 6):
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
        count = 0
        for payer in players:
            if(payer != player):
                count += 1
        player.payTax(price = count*50)
                
                
    def buildingLoan(player):
        player.addMoney(150)
        
        
    def crosswordWin(player):
        player.addMoney(100)
        

