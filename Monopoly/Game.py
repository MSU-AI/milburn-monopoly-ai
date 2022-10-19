import pygame


from Board import Board

pygame.init()
pygame.display.set_caption("Monopoly")


class Game:
    """
    Represents the playable Monopoly game.
    """

    WIDTH, HEIGHT = 600, 600

    def __init__(self):
        """
        Intializes Monopoly game.
        """
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        # TODO: When Board.draw is defined, draw the board.

def main():
    running = True
    game = Game()

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()
                
if __name__ == "__main__":
    main()
