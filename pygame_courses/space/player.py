from constants import *
from pygame.sprite import Sprite
from player_bullet import PlayerBullet
class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load\
            ("assets/space_ship.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        self.bullet_group = bullet_group
              
    def draw(self):
        screen.blit(self.image, self.rect)
    def fire(self)    :
        if len(self.bullet_group) < 2:
            PlayerBullet(self.rect.centerx, self.rect.top,\
                self.bullet_group)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5 