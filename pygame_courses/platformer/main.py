import pygame
from world import World
from level1 import world_data
from player import Player
pygame.init()

my_player = Player()
game_world = World(world_data)

screen_width = 1024
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen)
    my_player.draw(screen)
    my_player.move(game_world.tile_map)
    pygame.display.update()
    clock.tick(60)