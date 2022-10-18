
import pygame

pygame.init()

class Game:
    """
    Represents the playable Monopoly game.
    """

    WIDTH, HEIGHT = 800, 800

    def __init__(self):
        """
        Intializes Monopoly game.
        """
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

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
