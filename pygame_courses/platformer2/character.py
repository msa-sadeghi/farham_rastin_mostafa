from pygame.sprite import Sprite
import os
from config import *
import pygame.camera
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
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.all_images[animation] = temp
        self.image_number = 0
        self.action = self.animation_types[1]
        self.image = self.all_images[self.action][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_image_change_time = 0
        self.flip = False
        self.direction = 1
                
    def draw(self, screen):
        img = self.all_images[self.action][self.image_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)        
    
    def animation(self):
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.last_image_change_time = pygame.time.get_ticks()
        
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
    def move(self, moving_left, moving_right):
        dx = 0
        if moving_left:
            dx -= 5
            self.direction = -1
            self.flip = True
        if moving_right:
            dx += 5
            self.direction = 1
            self.flip = False
            
        self.rect.x += dx
    def change_action(self,new_animation):
        pass
                