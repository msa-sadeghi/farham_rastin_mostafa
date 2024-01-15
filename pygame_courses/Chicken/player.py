from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def draw(self):
        screen.blit(self.image, self.rect)
