from re import L
from Bank import Bank
from Board import Board
from Player import Player
import pygame
from time import sleep

# Initializes window and title
pygame.init()
pygame.display.set_caption("Monopoly")

class Game:
    """
    Represents the playable Monopoly game.
    """

    WIDTH, HEIGHT = 810, 810  # Window size

    def __init__(self):
        """
        Intializes the Monopoly game.
        """
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        #Banks probably predate the world

        self.bank = Bank()
        

    def drawBoard(self):
        """
        Draws game onto the window.
        """
        self.board.draw(self.window)


        pygame.display.update()
    
    def drawPlayers(self):
        
        padding = 20  # Distance between board and window
        board_width = self.window.get_width() - padding * 2  # Board width
        board_height = self.window.get_height() - padding * 2  # Board height
        for player in self.players:
            tile = self.board.board[player.position[0]][player.position[1]]
            player.currentTile(tile)
            tile.addPlayer()
            
            if player.position[0] == 0:
                    player.draw(
                        self.window,
                        padding + board_width - (player.position[1] + 1) * 70 + 5,
                        padding + board_height - 70
                    )
            elif player.position[0] == 1:
                player.draw(
                self.window,
                padding,
                padding + board_height - (player.position[1] + 1) * 70,

                )
            elif player.position[0] == 2:
                player.draw(
                    self.window,
                    padding + player.position[1] * 70,
                    padding
                )
            elif player.position[0] == 3:
                player.draw(
                    self.window,
                    padding + board_width - 70,
                    padding + player.position[1] * 70
                )
            
        pygame.display.update()
    def initBoard(self):
        self.board = Board(self.bank, self.players)
    #Needed to access the position of the tiles so I can calculate the rent correctly for the utility tiles
    def compareUtilites(self):
        electric = self.board[1][2]
        water = self.board[2][8]
        if electric.owner == water.owner:
            currentTile.getRent(player,diceroll * 10)
        else:
            currentTile.getRent(player,diceroll * 4)
    def initPlayers(self):
        print('Enter number of players[MIN 2-MAX 4]')
        self.players = []
        n = int(input(''))
        while(n <2 or n >4):
            print('Please enter between 2 and four players')
            print('Enter number of players[MIN 2-MAX 4]')
            n = int(input(''))
        for i in range(0,n):
            name = 'Player{}'.format(i)
            player = Player(name, 1000, self.bank)
            self.players.append(player)
def playerBankrupt(self, player):
    for row in player.properties:
        for tile in row:
            if(tile != 0):
                tile.Bankruptcy(self.bank)
                self.players.remove(player)
                self.bank.auctionProperty(tile, self.players)

    
# TODO : Add function for rolling dices to determine who goes first
def main():
    running = True
    game = Game()
    game.initPlayers()
    game.initBoard()
    game.drawBoard()
    game.drawPlayers()
    while len(game.players) > 1:
    
            
            
            
                


        # Event Loop -- all events (like key presses) are processed here
            for event in pygame.event.get():
                
                # On quit
                for player in game.players:
            
            
            
                    x = player.position[0]
                    y = player.position[1]
                    tile = game.board.board[x][y]
                    tile.removePlayer()
                    player.move()
                    x = player.position[0]
                    y = player.position[1]
                    tile = game.board.board[x][y]
                    tile.addPlayer()
                    game.drawBoard()
                    game.drawPlayers()
                    print(player.position)
                    print(player.name)
                    sleep(0.5)
                    
                    

                
                
                if event.type == pygame.QUIT:
                    running = False
    
    pygame.quit()
                
if __name__ == "__main__":
    main()
