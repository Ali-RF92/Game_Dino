import pygame
import sys
from dino import Dino

class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Dino Game')

        self.player1 = Dino((500,300))

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.player1.update(self.game_display)
                pygame.display.update()


new_game = Game()

