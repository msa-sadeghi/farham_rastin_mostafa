from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.velocity = 5

    def draw(self):
        screen.blit(self.image, self.rect)
    
    def reset(self):
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - 100:
            self.rect.y += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.velocity
