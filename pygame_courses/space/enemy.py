from constants import *
from pygame.sprite import Sprite
class Chick(Sprite):
    def __init__(self,x,y, chick_group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        chick_group.add(self)
        self.direction = 1
        self.speed = 5
        self.last_update_time = pygame.time.get_ticks()       
    def update(self):
        # if pygame.time.get_ticks() - self.last_update_time > 2000:
            self.rect.x += self.direction * self.speed
            # self.last_update_time = pygame.time.get_ticks()