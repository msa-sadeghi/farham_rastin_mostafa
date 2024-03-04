import pygame
class World:
    def __init__(self, world_data):
        self.tile_map = []
        bg_img = pygame.image.load("assets/background.png")
        self.bg_img = pygame.transform.scale(bg_img, (1024, 704))
        self.bg_rect = self.bg_img.get_rect(topleft=(0,0))
        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] == 1:
                    img = pygame.image.load("assets/dirt.png")
                    rect = img.get_rect(topleft = (j * 32, i * 32))
                    item = (img, rect)
                    self.tile_map.append(item)
                if world_data[i][j] == 2:
                    img = pygame.image.load("assets/grass.png")
                    rect = img.get_rect(topleft = (j * 32, i * 32))
                    item = (img, rect)
                    self.tile_map.append(item)
        
    def draw(self, screen):
        screen.blit(self.bg_img, self.bg_rect)
        for tile in self.tile_map:
            screen.blit(tile[0], tile[1])