import pygame
import sys
from dino import Dino
from constants import *
from ground import GND


class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(GAME_TITLE)
        self.font = pygame.font.Font(None, 22)
        self.hscore = self.load_high_score()
        self.score = 0
        self.ground = GND(5 , WINDOW_SIZE[1] - 150)
        self.player1 = Dino(DINO_INIT_LOCATION, self.fps) # Dino location in display
        self.clock = pygame.time.Clock()
        self.run()

    def load_high_score(self):
        with open("save.txt", "r") as file:
            hscore = file.read()
            return hscore

    def show_score(self, color):
        score = str(self.score)
        _score = self.font.render((6 - len(score)) * '0' + score , True, color)
        _hscore = self.font.render("HI: " + self.hscore, True, color)
        self.game_display.blit(_score, (910, 20))
        self.game_display.blit(_hscore, (800, 20))

    def new_score(self):
        if int(self.hscore) < self.score:
            with open("save.txt", "w") as file:
                _str = (6 - len(str(self.score))) * '0' + str(self.score)
                file.write(_str)

    def run(self):
        while True:
            self.game_display.fill(BLACK)
            self.show_score(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player1.jump()   
            
            self.ground.update(self.game_display)
            self.player1.update(self.game_display)
            pygame.display.update()
            self.score += 1
            self.clock.tick(self.fps)

new_game = Game()

