class Actions:
    
    def __init__(self, player, bank):
        self.player = player
        self.bank = bank

    def buyProperty(self, tile):
        if ((tile.type != 'Street') or (tile.type != '') or (tile.type != 'Railroad')\
            or (tile.type != 'Utility')):
            if(tile.owner == self.player):
                return False
            elif(tile.owner == self.player.bank):
                if(self.player.balance >= tile.price):
                    self.player.properties.append(tile)
                    tile.setOwner(self.player)
                    self.player.payMoney(tile.price)
                    return True
            else:
                return False 
        else:
            return False
    def unmortgageProperty(self, tile):
        if ((tile.type != 'Street') or (tile.type != '') or (tile.type != 'Railroad')\
            or (tile.type != 'Utility')):
            if(tile.owner != self.player):
                return False
            elif(tile.owner == self.player):
                if tile.is_mortgaged == False:
                    return False
                else:
                    if(self.player.balance >= tile.unMortgage()):
                        
                        self.player.balance.payMoney(tile.unMortgage())
                        return True
                    else:
                        return False
            else:
                return False
    def buildHouse(self, tile, board, group):
        min_t = 4
        indx = tile.group_list[group]
        if(tile.type == 'Street'):
            for t in board.group[indx]:
                if(t.checkAddHouseValidity(board)):
                    if(t.house_count <= min_t):
                        min_t = t
                        if(self.player.balance >= t.price_build):
                            self.player.payMoney(t.price_build)
                            t.addHouse(self.player)
                            return True
                        else:
                            return False
                else:
                    return False
        else:
            return False
            
    def buildHotel(self, tile, board, group):
        indx = tile.group_list[group]
        if(tile.type == 'Street'):
            for t in board.group[indx]:
                if(t.addHotelValidity(board)):
                    if(self.player.balance >= t.price_build):
                        self.player.payMoney(t.price_build)
                        t.addHotel()
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
            

    def mortgageProperty(self, tile, board, group):
        indx = tile.group_list[group]
        if ((tile.type != 'Street') or (tile.type != '') or (tile.type != 'Railroad')\
            or (tile.type != 'Utility')):
            if(tile.owner != self.player):
                return False
            else:
                if(tile.is_mortgaged == True):
                    return False
                else:
                    max_p = 0
                    max_t = 0
                    for t in board.group[indx]:
                        if(tile.mortgage_value >= max_p):
                            max_p = tile.mortgage_value
                            max_t = t
                    t.mortgage()
                    return True
    def sellHouse(self, tile, board, group):
        max_t = 0
        t_sell = 0
        if(tile.isCompletedGroup(board, self.player)):
            for t in board.group[group]:
                if(t.house_count >= max_t):
                    max_t = t.house_count
                    t_sell = t
            if(max_t > 0):
                t_sell.sellHouse(self.player)
                return True
        else:
            return False
    
    def sellHotel(self, tile, board, group):
        max_t = 0
        t_sell = 0
        if(tile.isCompletedGroup(board, self.player)):
            for t in board.group[group]:
                if(t.hotel_count >= max_t):
                    max_t = t.house_count
                    t_sell = t
            if(max_t > 0) and (self.bank.canSellHotel()):
                t_sell.sellHotel(self.player)
                return True
            else:
                return False
        else:
            return False

                

                
                

                    

            
            

    

    
        