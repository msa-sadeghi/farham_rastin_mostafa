from pygame.sprite import Sprite
import pygame

class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        self.gravity = -13
        group.add(self)
        
    def update(self):
        dx = self.direction * 4
        dy = self.gravity
        self.gravity += 1
        if self.rect.bottom + dy >= 300:
            dy = 300 - self.rect.bottom
            dx = 0
        
        
        self.rect.x += dx
        self.rect.y += dy
        