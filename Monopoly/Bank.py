from Tiles.Tile import Tile
from Tiles.StreetTile import StreetTile
from Tiles.RailroadTile import RailroadTile
from Tiles.UtilityTile import UtilityTile
import numpy as np
from Player import *
class Bank:
    """
    Represents the Monopoly bank.
    """
    def __init__(self):
        self.ownedProperty = []
        self.houses = 32
        self.hotel = 12
    """
    This function gets called inside the Board, when it gets initialized
    """
    def startOfGameOwnerShip(self, property):
        self.ownedProperty.append(self.ownedProperty, property)
    """
    Auction functionality
    """
    def auctionProperty(self, property, players):
        
        max_bid = dict({self : property.price})
        current_bid = dict()
        
        for player in players:
            current_bid[player] = player.bidAuction(property, max_bid)
            if(current_bid[player] > max_bid[list(max_bid.keys())[0]]):
                max_bid[player] = max_bid[list(max_bid.keys())[0]]
                max_bid[player] = current_bid[player]
                property.setOwner(player)
    
    def addHouse(self, n = 1):
        self.houses += n
    def sellHouse(self):
        self.houses -= 1
    def addHotel(self, n):
        self.hotel += n
    def sellHotel(self):
        self.hotel -= 1
        
                         





    
