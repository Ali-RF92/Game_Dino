import pygame

prefix = "./assets/"

class Dino():

    img_walk1 = pygame.image.load(prefix + "trex_run1.png")
    img_walk2 = pygame.image.load(prefix + "trex_run2.png")
    img_jump = pygame.image.load(prefix + "trex_jump.png")
    
    def __init__(self, location):
        self.location = location
        self.x_loc, self.y_loc = location


    def update(self, surface):
        surface.blit(self.img_walk1, self.location)
