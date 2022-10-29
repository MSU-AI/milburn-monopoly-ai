from re import L
from Bank import Bank
from Board import Board
from Player import Player
import pygame

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
        

    def draw(self):
        """
        Draws game onto the window.
        """
        self.board.draw(self.window)

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


def main():
    running = True
    game = Game()
    game.initPlayers()
    game.initBoard()
    while running:
        
        game.draw()
        
        # Event Loop -- all events (like key presses) are processed here
        for event in pygame.event.get():

            # On quit
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()
                
if __name__ == "__main__":
    main()
