import pygame
from world import World

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

world = World(0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    world.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)