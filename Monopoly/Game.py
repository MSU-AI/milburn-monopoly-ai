
from Board import Board

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

        self.board = Board()

    def draw(self):
        """
        Draws game onto the window.
        """
        self.board.draw(self.window, 20)

        pygame.display.update()
    
    #Needed to access the position of the tiles so I can calculate the rent correctly for the utility tiles
    def compareUtilites(self):
        electric = self.board[1][2]
        water = self.board[2][8]
        if electric.owner == water.owner:
            currentTile.getRent(player,diceroll * 10)
        else:
            currentTile.getRent(player,diceroll * 4)
def main():
    running = True
    game = Game()

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
