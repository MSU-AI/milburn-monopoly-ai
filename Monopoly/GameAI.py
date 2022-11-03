from re import L
from Bank import Bank
from Board import Board
from Player import Player
import pygame
from time import sleep
from Agent import Agent
from Actions import Actions
from RL.Action import Action
import matplotlib.pyplot as plt
from helper import plot
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
    """
    def compareUtilites(self):
        electric = self.board[1][2]
        water = self.board[2][8]
        if electric.owner == water.owner:
            currentTile.getRent(player,diceroll * 10)
        else:
            currentTile.getRent(player,diceroll * 4)
            """
    def initPlayers(self):
        
        self.players = []
        
        
        for i in range(0,2):
            name = 'Player{}'.format(i)
            player = Player(name, 1200, self.bank)
            self.players.append(player)
    def playerBankrupt(self, player):
        for row in player.properties:
            for tile in row:
                if(tile != 0):
                    tile.Bankruptcy(self.bank)
                    self.players.remove(player)
                    self.bank.auctionProperty(tile, self.players)
    
    def step(self, player, agent, n):
        done = False
        if (player.checkBankruptcy()) or (n >= 200):
            self.playerBankrupt(player)
            reward = -100
            done = True
        else:
            state_old = agent.getState(player, self.board.board)
            
            action= agent.getAction(state_old)
            

            self.actions[n%2].recieveAction([action])
            state_new = agent.getState(player, self.board.board)
            reward = player.possibleRent()
            agent.train_short_memory(state_old, action, reward, state_new, done)
            agent.remember(state_old, action[0], reward, state_new, done)
        return done
        
    


        
    def defActions(self):
        self.actions = []
        for player in self.players:
            action = Action(player, self.board, self.bank)
            self.actions.append(action)
    def reset(self):
        self.initPlayers()
        self.initBoard()
        self.defActions()
        self.bank = Bank()
        
    def getWinnerScore(self, players):
        return players[0].getWorth()

        
# TODO : Add function for rolling dices to determine who goes first
def main():
    running = True
    game = Game()
    record = 0
    score = 0
    mean_score = []
    scores = []
    total = 0
    game.initPlayers()
    game.initBoard()
    n = 2
    agent = Agent(game.board.board, game.bank)
    game.defActions()
    while True:
        done = False
        
        
        #print(game.players)
        game.players[n%2].move()
        done = game.step(game.players[n%2], agent, n)
        n += 1
        


        if done:
            print(agent.games)
            n = 2
            game.reset()
            agent.games += 1
            score = game.getWinnerScore(game.players)
            agent.trainLongMemory()
            if(score > record):
                record = score
                agent.model.save()
            scores.append(score)
            total += score
            mean_score.append(total / agent.games)
            plot(scores, mean_score)




        
                
                
                
                    


            # Event Loop -- all events (like key presses) are processed here
            for event in pygame.event.get():
                    
                    # On quit
                    
                        

                    
                    
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()
                
if __name__ == "__main__":
    main()
