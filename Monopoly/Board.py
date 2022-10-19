
class Tile:
    """
    Represents a tile on the board.
    """

    WIDTH, HEIGHT = 40, 40  # Tile size

    def __init__(self):
        """
        Initializes a Tile object.
        """

        # TODO: Save any specific tile attributes (property, jail, go, etc.)
        #       Will want to store the CSV data here somehow.
        
        self.players = set()  # Set of players currently on tile

class Board:
    """
    Represents the Monopoly game board.
    """
    
    WIDTH, HEIGHT = 750, 750  # Board size
    COLOR = (191, 219, 174)  # Board color
    LENGTH = 10  # The number of tiles on one side of the board.
    SIDES = 4  # The number of sides on the board.

    def __init__(self, window):
        """
        Initializes the game board.
        """
        self.window = window
        self.board = [Tile() for _ in range(self.LENGTH * self.SIDES)]

    def draw(self):
        """
        Draws the game board. 
        """
        self.window.fill(self.COLOR)

        # TODO: Draw individual tiles here, preferably similar to an actual
        #       Monopoly board (as rectangles around the perimeter).
        #       Hint: Take a look at pygame.draw.rect()!
