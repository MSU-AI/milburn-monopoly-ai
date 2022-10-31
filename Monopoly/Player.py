import random
from Actions import Action
import pygame
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
        self.properties = []
        self.property_value = 0
        self.movecount = 0
        self.bank = bank

        
    # TODO: FINISH METHODS BELOW
    def calculate_properties_value(self):
        for property in self.properties:
            if property.is_mortgaged == False:
                self.property_value += property.getMortVal()
    def move(self):
        self.rollDice()
        
        if(self.position[0]  + int((self.movecount + self.position[1]) / 10) > 3):
            self.position[0] = self.position[0] + int((self.movecount + self.position[1]) / 10) - 4
            self.position[1] = (self.position[1] + self.movecount) % 10
            self.addMoney(200)
        else:
            self.position[0] = int((self.movecount + self.position[1]) / 10) + self.position[0]
            self.position[1] = (self.position[1] + self.movecount) % 10
            
            
    
    def rollDice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        self.movecount = dice1+dice2

    def addMoney(self, money):
        self.balance += money  
    def payMoney(self, money):
        self.balance -= money
    def updatePos(self, pos):
        self.position = pos
    def getPos(self):
        return self.position
    def buyProperty(self, property, mortgages):
        if(self.balance - property.price >= 0):
            self.properties.append(property)
            self.payMoney(property.price)
        else:
            loan = (self.balance - property.price) * -1
            if self.checkBankruptcy(loan) == False:
                pass




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

    """
    Functions to check if player is bankrupt when he has to pay rent and 
    to add additional Debt
    """    
    def checkBankruptcy(self, extra = 0):
        if self.property_value + self.balance < self.money_owed + extra:
            return True
        else:
            return False
    def addDebt(self, loan):
        if(self.money_owed + loan <= self.property_value + self.balance):
            self.money_owed += loan
            self.balance += loan
            return True
        else:
            return False


    """Buy/Sell Houses/Hotels for your Tiles"""

    def sellHouse(self, property):
        self.balance += property.sellHouse()
        self.bank.addHouse()
    
    def sellHotel(self, tile):
        tile.sellHotel(self, self.bank)
    
    def buyHouse(self, tile):
        if(self.balance - tile.price_build >= 0):
            self.payMoney(tile.price_build)
            self.bank.sellHouse()
            tile.addHouse(self)
            return True
        else:
            return False
    
    def buyHotel(self, tile):
        if(self.balance - tile.price_build >= 0):
            self.payMoney(tile.price_build)
            self.bank.sellHouse()
            tile.addHotel(self)
            return True
        else:
            return False   


    # TODO: In future, a way to print out the property price and current bid
    def bid_Auction(property, max_bid):
        bid = int(input())
        return bid
    def currentTile(self, tile):
        self.tile = tile
    
    """Draws players depending on how many players are on a tile""" 
    def draw(self, window: pygame.Surface, x:int, y:int):
        board_width = window.get_width() - 20 * 2 
        board_height = window.get_height() - 20 * 2

        if(self.tile.players_on_tile == 1):
            pygame.draw.circle(
                window,
                (142, 14, 236),
                (x  + 10,y + 15),
                12,
                0
            )
        elif(self.tile.players_on_tile == 2):
            pygame.draw.circle(
                window,
                (142, 14, 236),
                (x + 46,y + 15),
                12,
                0
            )
        elif(self.tile.players_on_tile == 3):
            pygame.draw.circle(
                window,
                (142, 14, 236),
                (x + 10,y + 56),
                12,
                0
            )
        elif(self.tile.players_on_tile == 4):
            pygame.draw.circle(
                window,
                (142, 14, 236),
                (x + 46,y + 56),
                12,
                0
            )
    
    """Functions that are used in order print all possible actions every turn"""
    def printBuyableHouses(self, tiles):
        houses = dict()
        houses = """"""
        n =1 
        for tile in tiles:
            houses[n] = tile
            n += 1
        print('H + Index')
        for tile in houses:
            houses +=('Index : {} Name : {} Price: {} Houses:{}\n'.format(tile, houses[tile].name, houses[tile].price_build, \
                houses[tile].house_count))
        return houses 
        
    def printBuyableHotels(self, hotels):
        print('L + Index')
        hotels = """"""
        for index, tile in enumerate(hotels):
            hotels += ('Index : {} Name : {} Price: {} Houses:{}\n'.format(index, tile.name, tile.price_build, \
                tile.house_count))
        return hotels
    def printMortgage(self, tiles, required = 0):
        print('Press M + Index')
        mortgages = """"""
        for index , tile in enumerate(tiles):
            if(tile.getMortVal() >= required):
                mortgages += ('Index : {} Name : {} Return: {} Houses: {} Hotels: {}\n'.format(\
                    index, tile.name, tile.getMortVal(), tile.house_count, tile.hotel_count))
        return mortgages
    """Execution of a Players Turn"""
    # TODO: Break this into smaller functions
    def action(self,tile, game):
        

        print('Press N to End Turn')
        while(pygame.key.get_pressed()[pygame.K_n] == False):
            houses = self.possibleHouses(game.board)
            hotels = self.possibleHotels(game.board)
            mortgages = self.possibleMortgages()
            self.buyProperty(tile, mortgages)
            self.printHouses(houses)
            self.printHotels(hotels)
            self.printMortgage()
            if (pygame.key.get_pressed()[pygame.K_h]):
                index = int(input('Choose an index'))
                self.printHouses()
                if self.buyHouse(houses[index]) == False:
                    loan = self.balance - houses[index].price_build
                    if self.checkBankruptcy(loan) == False:
                        option = input('D-Add Debt to Buy, M-To Mortgage')
                        while(option != 'D' or option != 'M'):
                            if(option == 'D'):
                                res = self.addDebt(loan)
                                self.buyHouse(houses[index])
                                
                            elif(option == 'M'):
                                self.printMortgage(mortgages, loan)
                                index = int(input('Choose an index'))
                                mortgages[index].mortgage(self)
                                self.buyHouse(houses[index])
                    else:
                        
                        print('You are unable to buy this house as you cannot add more debt')
                        
 
                else:
                    pass




                    
            elif(pygame.key.get_pressed()[pygame.K_l]):
                index = int(input('Choose an index'))
                hotels[index].addHotel(self)
            elif(pygame.key.get_pressed()[pygame.K_m]):
                index = int(input('Choose an index'))
            elif(pygame.key.get_pressed()[pygame.K_n]):
                break
        print('Turn ended')

    """Checks for all Tiles that can add a house/hotel or they can be mortgaged"""
    def possibleHouses(self, board):
        tiles = []
        for tile in self.properties:
            if(tile.is_mortgaged == False):
                if tile.checkAddHouseValidity(board):
                    tiles.append(tile)
        return tiles
    def possibleHotels(self, board):
        tiles = []
        for tile in self.properties:
            if(tile.is_mortgaged == False):
                if tile.addHotelValidity(board):
                    tiles.append(tile)
        return tiles
    def possibleMortgages(self):
        tiles = []
        n = 1
        for tile in self.properties:

            if tile.is_mortgaged == False:
                tiles.append(tile)
        return tiles
    def sellableHouses(self, required = 0):
        tiles = []
        for tile in self.properties:
            if tile.house_count * tile.price_build / 2 >= required:
                tiles.append(tile)
        return tiles
    
    def sellableHotels(self, required = 0):
        tiles = []
        for tile in self.properties:
            if tile.hotel_count * tile.price_build / 2 >= required:
                tiles.append(tile)
        return tiles
    # TODO: Create visual buttons for all of these that are printed out in the window
    """
    Function that runs a process of a turn for each player
    """
    def myTurn(self, game):
        if(self.in_jail == False):
            self.rollDice()
            x = self.position[0]
            y = self.position[1]
            tile = game.board.board[x][y]
            
            if(tile.owner != self and tile.owner == game.bank):
                yn = input('Would you like to buy the property: Y/N')
                if(yn == 'Y'):
                    

                    
                    self.action(tile, game)
                else:
                    game.bank.auctionProperty(tile, game.players)
            elif(tile.owner != self):
                rent = tile.calcRent()
                print('You have to pay {} ${} for rent'.format(tile.owner.name, ))
                if(self.checkBankruptcy(tile.calcRent()) == True):
                    game.playerBankrupt(self)
                else:
                    if(self.balance < rent):
                        print('You have to either take out a loan of {} or mortgage one of your properties'.format(
                            rent - self.balance))
    






