from pygame.sprite import Sprite
import pygame
class Coin(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/img/coin.png")
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect(topleft = (x,y))
        group.add(self)
        self.counter = 0
        self.direction = 1
        
    def update(self):
        self.counter += 1
        self.rect.y += self.direction
        if self.counter >= 30:
            self.counter *= -1
            self.direction *= -1