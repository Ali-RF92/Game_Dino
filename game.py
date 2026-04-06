import pygame
import sys

pygame.init()
game_display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Dino Game')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()