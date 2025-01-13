from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, owner, x,y, direction, group):
        super().__init__()
        self.owner = owner
        self.direction = direction
        self.image = pygame.image.load("./assets/images/icons/bullet.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        
    def update(self):
        self.rect.x += self.direction * 4
        if self.rect.x <= 0 or self.rect.x >= 800:
            self.kill()
            