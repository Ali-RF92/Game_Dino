import pygame
from random import randint as rnd
prefix = "./assets/"


class Obstacles:
    def __init__(self, y, min_gap, speed):
        self.obs_list = []
        self.y = y
        self.min_gap = min_gap
        self.speed = speed
        self.init_obss()

    def init_obss(self):
        self.obs_list.append(Obstacle((rnd(700, 1000), self.y), self.speed ))
        self.obs_list.append(Obstacle((rnd(1450, 1750), self.y), self.speed ))
        self.obs_list.append(Obstacle((rnd(2200, 2500), self.y), self.speed ))

    def remove(self):
        self.obs_list.pop(0)

    def generate_obs(self):
        self.obs_list.append(Obstacle((rnd(2000,2300), self.y), self.speed))

    def check(self):
        if self.obs_list[0].x_loc + self.obs_list[0].width < 0:
            self.remove()
        if self.obs_list[-1].x_loc+self.obs_list[-1].width+self.min_gap<2000:
            self.generate_obs()

    def update(self, Surface):
        for obs in self.obs_list:
            obs.update(Surface)

class Obstacle:
    img_list = [
        ["tree1s3.png"],
        ["tree2s3.png"],
        ["tree3s3.png"]
    ]
    def __init__(self, location, speed):
        self.location = location
        self.x_loc, self.y_loc = location
        self.speed = speed
        self.type = rnd(0, len(self.img_list) - 1)
        self.img = pygame.image.load(prefix+self.img_list[self.type][0])
        self.width = self.img.get_width()
        self.rect = self.img.get_rect()



    def update(self, Surface):
        self.x_loc -= self.speed
        Surface.blit(self.img, (self.x_loc, self.y_loc))