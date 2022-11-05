import numpy as np
import pygame
import random
from Tiles.Tile import Tile
from Player import Player
from Tiles.JailTile import JailTile
class ChestTile(Tile):
    """
    Represents a "Community Chest" tile on the board.
    """

    def __init__(self, attributes, players):
        """
        Initializes the "Community Chest" tile.
        """
        #self.deck = []
        self.players = players
        self.color = 'DarkGreen'
        self.name = 'Chance'
        self.type = attributes['Space']
        self.owner = "Bank"
        super().__init__()
    def goToGo(player):
        
        player.updatePos([0,0])
        player.getMoney(200)
    def bankError(player):
        player.addMoney(200)
    def doctorsFees(player):
        player.payTax(50)
    def getOutOfJail(player):
        player.addGetOutOfJail()
    def goToJail(player):
        player.updatePos([1,0])
    """
    Collects 50 from all players
    """
    def grandOperaNight(player, players):
        for payer in players:
            if(payer != player):
                payer.payTax(player, 50)

    def Holiday(player):
        player.addMoney(200)
    def incomeTaxRefund(player):
        player.addMoney(200)
    def yourBirthday(player, players):
        for payer in players:
            if(payer != player):
                payer.payTax(player, 10)
    def insuranceMatures(player):
        player.addMoney(100)
    def hospitalFees(player):
        player.payTax(price = 50)
    def schoolFees(player):
        player.payTax(price = 50)
    def consultancyFee(player):
        player.addMoney(25)
    # TODO: Add a separate attributes in player class in order to make this function a lot easier
    def streetRepairs(player):
        player.payTax(price = player.houses * 40 + player.hotels * 115)
    def beautyContest(player):
        #Only second place tho :(
        player.addMoney(10)
    def inheritMoney(player):
        player.addMoney(100)
    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS[self.color],
            (x, y, self.WIDTH, self.HEIGHT)
        )
    
