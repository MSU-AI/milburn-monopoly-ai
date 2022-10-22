
from Tiles.Tile import Tile

import pygame

class StreetTile(Tile):
    """
    Represents a street tile in the Monopoly game.
    """

    def __init__(self, attributes: dict):
        """
        Initializes a street tile.
        """
        super().__init__()

        # Constant attributes
        self.name = attributes['Name']
        self.color = attributes['Color']
        self.tile_price = attributes['Price']
        self.build_price = attributes['PriceBuild']
        self.rent = (
            attributes['Rent'],
            attributes['RentBuild1'],
            attributes['RentBuild2'],
            attributes['RentBuild3'],
            attributes['RentBuild4'],
            attributes['RentBuild5']
        )

        # Dynamic attributes
        self.owner = None
        self.house_count = 0
        self.hotel_count = 0
        # self.mortgage_value = mortgage_value
        # self.is_mortgaged = False

    def draw(self, window: pygame.Surface, x: int, y: int):
        """
        Draws the tile onto a specified window.
        """
        pygame.draw.rect(
            window,
            self.COLORS[self.color],
            (x, y, self.WIDTH, self.HEIGHT)
        )

    # set the owner to a Player object
    def setOwner(self, Player):
        self.owner = Player

    def addHouse(self):
        while self.house_count <= 4:
            self.house_count += 1

    def getWorth(self):
        # worth of a property if it has 1, 2, 3, or 4 houses
        # brown & light blue: $50/house
        # purple & orange: $100/house
        # red & yellow: $150/house
        # green & blue: $200/house
        if self.house_count != 0:
            if self.color_group == 'brown' or self.color_group == 'light blue':
                return self.price + self.house_count * 50 / 2
            elif self.color_group == 'purple' or self.color_group == 'orange':
                return self.price + self.house_count * 100 / 2
            elif self.color_group == 'red' or self.color_group == 'yellow':
                return self.price + self.house_count * 150 / 2
            else:
                return self.price + self.house_count * 200 / 2

        # worth of a property if it has 1 hotel (cost of 1 hotel = 1 house)
        elif self.house_count == 0 and self.hotel_count == 1:
            if self.color_group == 'brown' or self.color_group == 'light blue':
                return self.price + (self.house_count + 1) * 50 / 2
            elif self.color_group == 'purple' or self.color_group == 'orange':
                return self.price + (self.house_count + 1) * 100 / 2
            elif self.color_group == 'red' or self.color_group == 'yellow':
                return self.price + (self.house_count + 1) * 150 / 2
            else:
                return self.price + (self.house_count + 1) * 200 / 2

        # worth of a property if it has 0 house and 0 hotel
        else:
            return self.price

    def sellHouse(self):
        if self.house_count >= 1 and self.hotel_count <= 4:
            self.house_count -= 1

    def addHotel(self):
        if self.house_count == 4:
            self.hotel_count = 1
            self.house_count = 0

    def sellHotel(self):
        self.hotel_count = 0

    def mortgage(self):
        if self.house_count == 0 and self.hotel_count == 0:
            self.is_mortgaged = True

    def unMortgage(self):
        self.is_mortgaged = False

    def calcRent(self):
        if self.hotel_count == 0:
            return self.rent[self.house_count]
        elif self.hotel_count == 1:
            return self.rent[-1]