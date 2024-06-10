from pygame.sprite import Sprite
import pygame
class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.images = []
        for i in (25, 50, 100):
            img = pygame.image.load(f"assets/castle/castle_{i}.png")
            img_w = img.get_width()
            img_h = img.get_height()
            img = pygame.transform.scale(img, (img_w * 0.3, img_h * 0.3))
            self.images.append(img)
            
        self.image = self.images[2]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.health = 1000
        self.max_health = 1000
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    #