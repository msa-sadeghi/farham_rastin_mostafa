from pygame.sprite import Sprite
import os
from config import *
class Character(Sprite):
    def __init__(self, type, x,y, ammo, grenades):
        super().__init__()
        self.type = type
        self.ammo = ammo
        self.grenades = grenades
        self.alive = True
        self.health = 100
        self.max_health = 100
        self.animation_types = os.listdir(f"assets/images/{self.type}")
        self.all_images = {}
        for animation in self.animation_types:
            temp = []
            num_of_files = len(os.listdir(f"assets/images/{self.type}/{animation}"))
            for i in range(num_of_files):
                img = pygame.image.load(f"assets/images/{self.type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 1.5, img_h * 1.5))
                temp.append(img)
            self.all_images[animation] = temp
        self.image_number = 0
        self.action = self.animation_types[1]
        self.image = self.all_images[self.action][0]
        self.rect = self.image.get_rect(topleft=(x,y))
                
    def draw(self, screen):
        screen.blit(self.image, self.rect)        
        