from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/img/guy{i}.png")
            self.right_images.append(img)
            left_img = pygame.transform.flip(img, True, False)
            self.left_images.append(left_img)
        self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft = (100, 500))
        self.alive=True
        self.score=0
        self.health=3
        self.yvelocity=0
        self.xvelocity=5
        self.direction =   1 
        self.jumped = False
    def draw(self,screen):
        screen.blit(self.image, self.rect)       
    def move(self, tile_map):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            dx -= self.xvelocity
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            dx += self.xvelocity
        if keys[pygame.K_SPACE] and not self.jumped:
            self.yvelocity = -13
            self.jumped = True
        dy += self.yvelocity
        self.yvelocity += 1
        
        for tile in tile_map:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y , self.image.get_width(), self.image.get_height()):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                if self.yvelocity > 0:
                    self.yvelocity = 0
                    dy = tile[1].top - self.rect.bottom
                    self.jumped = False
                else:
                    self.yvelocity = 0
                    dy = tile[1].bottom - self.rect.top
            
        self.rect.x += dx
        self.rect.y += dy
        
            
            
        