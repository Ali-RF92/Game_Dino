import pygame


class Day_Or_Night:
    def __init__(self, fps, length):
        self.threshold = fps * length
        self.counter = 0
        self.state = True
        self.clr = 0
        self.transition_speed = 2
        self.transition = False

    def update(self, Surface):
        _max = 255-self.transition_speed
        _min = 0-self.transition_speed
        if self.transition:
            self.clr += self.transition_speed   
        if self.clr >= _max or self.clr < _min:
            self.transition_speed *= -1
            self.transition = False
        Surface.fill((self.clr, self.clr, self.clr))
        self._update()
        return (255,255,255) if self.transition_speed > 0 else (0,0,0)

    def _update(self):
        if not self.transition:
            if self.counter >= self.threshold:
                self.transition = True
                self.counter = 0
            else:
                self.counter += 1
