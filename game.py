import pygame
import sys
from dino import Dino

class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Dino Game')

        self.player1 = Dino((100,390), self.fps) # Dino location in display
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):

        rect1 = pygame.Rect(800, 150, 50, 50)
        ground = pygame.image.load("./assets/desert.png")

        while True:
            self.game_display.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player1.jump()

            rect1.x -= 1
            pygame.draw.rect(self.game_display, (255,255,255), rect1)
            if rect1.colliderect(self.player1.rect):
                print("Collision")
            else:
                print("No Collision")
            
            self.game_display.blit(ground, (0, 450)) # Ground location in display
            self.player1.update(self.game_display)

            #
            pygame.display.update()

            self.clock.tick(self.fps)

new_game = Game()

