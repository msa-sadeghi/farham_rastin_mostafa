import pygame
from world import World
from level1 import world_data
from player import Player
from button import Button


pygame.init()

my_player = Player()
enemy_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group)
pygame.mixer.music.load("assets/img/music.wav")
pygame.mixer.music.play(-1)
screen_width = 1024  
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

restart_image = pygame.image.load("assets/img/restart_btn.png")
restart_button = Button(restart_image, screen_width/2, screen_height/2)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    my_player.draw(screen)
    my_player.move(game_world.tile_map, enemy_group)
    if not my_player.alive:
        restart_button.draw(screen)
        if restart_button.check_click():
            my_player.__init__()
    pygame.display.update()
    clock.tick(60)