from pygame.sprite import Sprite
import pygame

from explosion import Explosion

class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        self.gravity = -13
        group.add(self)
        self.timer = 100
        
    def update(self, explosion_group):
        dx = self.direction * 4
        dy = self.gravity
        self.gravity += 1
        if self.rect.bottom + dy >= 300:
            dy = 300 - self.rect.bottom
            dx = 0
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(self.rect.centerx , self.rect.centery, explosion_group)
        
        self.rect.x += dx
        self.rect.y += dy
        