from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, type, x,y, health, group, speed):
        super().__init__()
        self.type = type
        self.health = health
        self.max_health = health
        self.speed = speed
        self.alive = True
        group.add(self)
        self.animation_types = ("walk", "attack", "death")
        self.all_images = {}
        for action in self.animation_types:
            images = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{type}/{action}/{i}.png")
                imh = img.get_height()
                imw = img.get_width()
                img = pygame.transform.scale(img, (imw, imh))
                images.append(img)
            self.all_images[action] = images
        self.image = self.all_images['walk'][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.action = "walk"
        self.image_number = 0
            
        