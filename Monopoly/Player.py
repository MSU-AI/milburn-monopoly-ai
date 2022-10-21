from Bank import Bank
from Board import Board
from Property import Property
import random
class Player:
    # TODO: initialize the player so that he has default starting money, position
    # TODO: Also initialize list for properties 
    def __init__(self, name, balance, position, money_owed, bankrupt):
        self.name = name
        self.balance = balance
        self.position = position
        self.money_owed = money_owed
        self.bankrupt = False
        self.properties = []
        self.property_value = 0
        self.calculate_properties_value()
        pass
    # TODO: FINISH METHODS BELOW
    def calculate_properties_value(self):
        for property in self.properties:
            self.property_value += property.value
    
    def rollDice():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        movecount = dice1+dice1
        
    def updatePos():
        pass
    def buyProperty(property):
        self.properties.append(property)
    def sellProperty():
        self.properties.remove(property)
    def drawCommunity_Chest():
        pass
    def drawChance():
        pass
    def payRent():
        pass
    def payTax():
        pass
    def recieveGo():
        pass
    def getWorth():
        pass
    def mortgage():
        pass
    def unMortgage():
        pass
    def checkBankruptcy(self):
        if self.property_value + balance < self.money_owed:
            self.bankrupt = True
    def addDebt():
        pass
    def sellHouse():
        pass
    def sellHotel():
        pass
    def buyHouse():
        pass
    def buyHotel():
        pass
    # TODO: In future, a way to print out the property price and current bid
    def bid_Auction(property, max_bid):
        bid = int(input())
        return bid
    pass
