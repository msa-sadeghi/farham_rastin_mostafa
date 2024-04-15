from pygame.sprite import Sprite
import pygame
class Door(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/img/exit.png")
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect(topleft = (x,y))
        group.add(self)
        
        
