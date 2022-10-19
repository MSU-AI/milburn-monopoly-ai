
import pygame

from Board import Board

pygame.init()
pygame.display.set_caption("Monopoly")

class Game:
    """
    Represents the playable Monopoly game.
    """

    WIDTH, HEIGHT = 800, 800  # Window size

    def __init__(self):
        """
        Intializes Monopoly game.
        """
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def draw(self):
        """
        Draws game onto window.
        """
        # Draws board
        board = Board(self.window)
        board.draw()

        pygame.display.update()

def main():
    running = True
    game = Game()

    while running:
        game.draw()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()
                
if __name__ == "__main__":
    main()
