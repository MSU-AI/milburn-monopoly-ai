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
        self.position = position #[0,0] initially
        self.money_owed = money_owed
        self.bankrupt = False
        self.properties = []
        self.property_value = 0
        self.movecount = 0
        self.calculate_properties_value()
        pass
    # TODO: FINISH METHODS BELOW
    def calculate_properties_value(self):
        for property in self.properties:
            self.property_value += property.value
    def move(self):
        self.rollDice()
        if self.position[1] + self.movecount <= 9:
            self.position[1] += self.movecount
         elif self.position[1] + self.movecount >9 and self.position[1] + self.movecount < 20:
            if self.position[0]<3:
                self.position[0]+=1
            else:
                self.position[0] = 3
                self.position[1] = 20 - (position[1]+ self.movecount)
         else:
            if self.position[0] <2:
                self.position[0]+=1
            elif self.position[0] == 2:
                self.position[0] = 1
            else:
                self.position[0] = 2
            self.position[1] = self.position[1] + self.movecount -20
            
            
    
    def rollDice():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        self.movecount = dice1+dice1

        
    def updatePos():
        pass
    def buyProperty(property):
        self.properties.append(property)
    def sellProperty():
        self.properties.remove(property)
    def drawCommunity_Chest():
        community_chest.draw()
    def drawChance():
        chance.draw()
    def payRent(property_landed_on):
        balance -= property_landed_on.rent
    def mortgage(self, property_mortgage):
        self.balance += property_morgage.value/2
    def unMortgage(self, property_unmortgage):
        self.balance -= property_unmortgage/2 + property_unmortgage*0.1
        
    def checkBankruptcy(self):
        if self.property_value + balance < self.money_owed:
            self.bankrupt = True
    def addDebt(self, owe):
        self.money_owed += owe
    def sellHouse(self, property):
        property_of_house_to_sell = next((obj for obj in self.properties if obj.name == property),None)
        self.balance += property_of_house_to_sell.houses.value/2
        property_of_house_to_sell.houses_available.append(hotel)
    def sellHotel(self, hotel):
        property_of_hotel_to_sell = next((obj for obj in self.properties if obj.name == property),None)
        self.balance += property_of_hotel_to_sell.hotels.value/2
        property_of_hotel_to_sell.houses_available.append(hotel)
    def buyHouse(self, house):
        property_of_house_to_sell = next((obj for obj in self.properties if obj.name == property),None)
        self.balance -= property_of_house_to_sell.house.value
        property_of_house_to_buy.houses_available.remove(house)
    def buyHotel():
        property_of_hotel_to_sell = next((obj for obj in self.properties if obj.name == property),None)
        self.balance -= property_of_hotel_to_sell.hotel.value
        property_of_hotel_to_buy.hotels_available.remove(hotel)    
    # TODO: In future, a way to print out the property price and current bid
    def bid_Auction(property, max_bid):
        bid = int(input())
        return bid
    pass
