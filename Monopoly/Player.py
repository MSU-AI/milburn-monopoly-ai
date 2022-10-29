import random
import numpy as np
class Player:
    # TODO: initialize the player so that he has default starting money, position
    # TODO: Also initialize list for properties 
    def __init__(self, name, balance, bank):
        self.name = name
        self.balance = balance
        self.position = [0,0] #[0,0] initially
        self.money_owed = 0
        self.bankrupt = False
        a = np.zeros((4,10), dtype = int)
        a = [list(a[0]),list(a[0]),list(a[0]),list(a[0])]
        self.properties = a
        self.property_value = 0
        self.movecount = 0
        self.bank = bank

        
    # TODO: FINISH METHODS BELOW
    def calculate_properties_value(self):
        for property in self.properties:
            self.property_value += property.value
    def move(self):
        self.rollDice()
        if(self.pos[0]  + int((self.movecount + self.pos[1]) / 10) > 3):
            self.pos[0] = int((self.movecount + self.pos[1]) / 10) - 4
            self.pos[1] = (self.pos[1] + self.movecount) % 10
            self.addMoney(200)
        else:
            self.pos[0] = int((self.movecount + self.pos[1]) / 10) + self.pos[0]
            self.pos[1] = (self.pos[1] + self.movecount) % 10
            
            
    
    def rollDice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        self.movecount = dice1+dice1

    def addMoney(self, money):
        self.balance += money  
    def payMoney(self, money):
        self.balance -= money
    def updatePos():
        pass
    def buyProperty(self, property):
        x = self.position[0]
        y = self.position[1]
        self.properties[x][y] = property
    """
    This function will be added in the future 
    def sellProperty(self, tile, player, offer):
        self.properties[tile.position[0]][tile.position[1]] = 0
        self.balance += offer
        player.properties[tile.position[0]][tile.position[1]] = tile
        tile.setOwner(player)
        player.payMoney(self, offer)
    """
    def drawCommunity_Chest(self, board):
        board.drawChance(self)
    def drawChance(self, board):
        board.drawCommunity_Chest(self)
    def payRent(self, tile):
        self.balance -= tile.calcRent()
        tile.owner.addMoney(tile.calcRent())
    def mortgage(self, tile):
        self.balance += tile.mortgage_value
    def unMortgage(self, tile):
        self.balance -= tile.unMortgage()

        
    def checkBankruptcy(self):
        if self.property_value + self.balance < self.money_owed:
            self.bankrupt = True
    def addDebt(self, loan):
        self.money_owed += loan
        self.balance += loan
    def sellHouse(self, property):
        self.balance += property.sellHouse()
        self.bank.addHouse()
    def sellHotel(self, tile):
        tile.sellHotel(self, self.bank)
    def buyHouse(self, tile):
        tile.addHouse(self)
    def buyHotel(self, tile):
        tile.addHotel(self)    
    # TODO: In future, a way to print out the property price and current bid
    def bid_Auction(property, max_bid):
        bid = int(input())
        return bid
    def draw():
        pass
