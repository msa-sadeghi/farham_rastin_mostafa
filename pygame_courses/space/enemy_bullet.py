from pygame.sprite import Sprite
from constants import *
class EnemyBullet(Sprite):
    def __init__(self, x,y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/enemy_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        bullet_group.add(self)
        
    def update(self):
        self.rect.y += 5
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()