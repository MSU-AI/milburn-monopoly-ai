from xml.dom.xmlbuilder import DocumentLS
from Actions import Actions

class Action:
    def __init__(self, player, board, bank):
        
        self.player = player
        self.board = board
        self.bank = bank
        self.actions = Actions(self.player, bank)

    def recieveAction(self, pactions):
        #print(pactions[0][0])
        self.action = pactions[0][0].index(1)
        self.group = pactions[0][1]
        tile = self.board.board[self.player.position[0]][self.player.position[1]]
        
        if (self.action == 1):
            if ((tile.type == 'Street') or  (tile.type == 'Railroad')\
            or (tile.type == 'Utility')):
                if(tile.color == self.group):
            
                    self.spendOnTile(tile)
                else:
                    self.spendOnGroup(tile)
            else:
                self.spendOnGroup(tile)
        elif(self.action ==  -1):
            self.getMoneyFromGroup(tile)
        

    def spendOnTile(self, tile):
        if(self.actions.buyProperty(tile) == False):
            if(self.actions.unmortgageProperty(tile) == False):
                self.actions.buildHouse(tile, self.board, self.group)
                self.actions.buildHotel(tile, self.board, self.group)

    def spendOnGroup(self, tile):
        done = False
        if ((tile.type == 'Street') or  (tile.type == 'Railroad')):
            for t in self.board.group[tile.color]:
                if(self.actions.unmortgageProperty(tile) == True):
                    done = True
                    break
            if not done:
                self.actions.buildHouse(tile, self.board, tile.group)
                self.actions.buildHotel(tile,self.board, tile.group)
    def getMoneyFromGroup(self, tile):
        if ((tile.type == 'Street') or  (tile.type == 'Railroad')):
            if(self.actions.sellHouse(tile, self.board, self.group) == False):
                if self.actions.mortgageProperty(tile, self.board, self.group):
                    pass
            else:
                self.actions.sellHotel(tile, self.board, self.group)
                    

        

