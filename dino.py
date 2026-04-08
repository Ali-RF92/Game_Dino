import pygame

prefix = "./assets/"

class Dino():

    img_walk1 = pygame.image.load(prefix + "trex_run1.png")
    img_walk2 = pygame.image.load(prefix + "trex_run2.png")
    img_jump = pygame.image.load(prefix + "trex_jump.png")

    def __init__(self, location,fps):
        self.location = location
        self.x_loc, self.y_loc = location
        self.Y_LOC = self.y_loc
        self.fps = fps
        self.walk_img = True
        self.walk_slicer = 8
        self.walk_counter = 0
        self.state = True
        self.jump_threshold = self.y_loc - 200
        self.YD = 5
        self.yd = self.YD
        self.rect = self.img_walk1.get_rect(topleft = self.location)

    def update(self, surface):
        if self.state:
            if self.walk_counter < self.fps:
                if self.walk_counter % self.walk_slicer == 0:
                    self.walk_img = not self.walk_img
                self.walk_counter += 1

            else:
                self.walk_counter = 0

            if self.walk_img:
                surface.blit(self.img_walk1, self.location)
            else:
                surface.blit(self.img_walk2, self.location)

        else:
            if self.yd > 0: # going up
                if self.y_loc < self.jump_threshold:
                    self.yd *= -1

            else: # going down
                if self.y_loc > self.Y_LOC:
                    self.state = True
                    self.yd = self.YD
            
            self.y_loc -= self.yd
            surface.blit(self.img_jump, (self.x_loc, self.y_loc))
            self.rect.topleft = (self.x_loc, self.y_loc)


        
    def jump(self):
        self.state = False



