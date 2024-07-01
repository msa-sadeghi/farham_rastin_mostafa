from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.speed = 4
        group.add(self)
        
        
    def update(self):
        
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += -self.speed * math.sin(self.direction)
        if self.rect.left < 0 or self.rect.right > 800 or self.rect.top > 600 or self.rect.bottom < 0:
            self.kill()