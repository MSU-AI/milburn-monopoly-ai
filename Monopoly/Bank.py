import Property
import numpy as np
from Player import *
class Bank:
    """
    Represents the Monopoly bank.
    """
    def __init__(self):
        self.ownedProperty = np.array()
    """
    This function gets called inside the Board, when it gets initialized
    """
    def startOfGameOwnerShip(self, property):
        np.append(self.ownedProperty, property)
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
                          





    
