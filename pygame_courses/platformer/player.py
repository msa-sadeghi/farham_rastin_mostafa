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
        self.moving_state = False
        self.update_time = pygame.time.get_ticks()
        self.jump_sound = pygame.mixer.Sound("assets/img/jump.wav")
        self.coin_sound = pygame.mixer.Sound("assets/img/coin.wav")
        self.dead_image = pygame.image.load("assets/img/ghost.png")
        
    def draw(self,screen):
        if not self.alive:
            self.image = self.dead_image
        screen.blit(self.image, self.rect) 
        self.animation()
    def animation(self):
        if pygame.time.get_ticks() - self.update_time > 200:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.right_images) or not self.moving_state:
            self.frame_index = 0
        if self.direction == 1:
            self.image = self.right_images[self.frame_index]
        elif self.direction == -1:
            self.image = self.left_images[self.frame_index]        
    def move(self, tile_map, enemy_group, coin_group):
        dx = 0
        dy = 0
        if self.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.moving_state = True
                self.direction = -1
                dx -= self.xvelocity
            if keys[pygame.K_RIGHT]:
                self.moving_state = True
                self.direction = 1
                dx += self.xvelocity      
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.moving_state = False
            
            if keys[pygame.K_SPACE] and not self.jumped:
                self.jump_sound.play()
                self.yvelocity = -15
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
            if pygame.sprite.spritecollide(self, enemy_group, False)    :
                self.alive=False
            if pygame.sprite.spritecollide(self, coin_group, True)    :
                self.score += 1
                self.coin_sound.play()
            self.rect.x += dx
            self.rect.y += dy
        
            
            
        