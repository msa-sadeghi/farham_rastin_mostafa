import pygame
from world import World

from player import Player
from button import Button

import pickle
pygame.init()

f = open("level1", "rb")
world_data = pickle.load(f)

level = 1
MAX_LEVEL = 3
my_player = Player()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group, coin_group, door_group)
pygame.mixer.music.load("assets/img/music.wav")
pygame.mixer.music.play(-1)
screen_width = 1024  
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

restart_image = pygame.image.load("assets/img/restart_btn.png")
restart_button = Button(restart_image, screen_width/2, screen_height/2)

def check_level_completed():
    global level
    if pygame.sprite.spritecollide(my_player, door_group, False):
        if level < 3:
            level += 1
        f = open(f"level{level}", "rb")
        world_data = pickle.load(f)
        my_player.__init__()
        coin_group.empty()
        enemy_group.empty()
        door_group.empty()
        game_world = World(world_data, enemy_group, coin_group, door_group)
        return game_world
        


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    check_level_completed()
    game_world.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    door_group.update()
    door_group.draw(screen)
    my_player.draw(screen)
    my_player.move(game_world.tile_map, enemy_group, coin_group)
    if not my_player.alive:
        restart_button.draw(screen)
        if restart_button.check_click():
            coin_group.empty()
            enemy_group.empty()
            door_group.empty()
            game_world = World(world_data, enemy_group, coin_group,door_group)
            my_player.__init__()
    pygame.display.update()
    clock.tick(60)