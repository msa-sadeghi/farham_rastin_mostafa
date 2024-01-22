from constants import *
from player import Player
from egg import Egg
import random
clock = pygame.time.Clock()
FPS = 60
level = 0
egg_group = pygame.sprite.Group()
my_player = Player(martin_img, SCREEN_WIDTH / 2, SCREEN_HEIGHT)
def start_new_level():
    global level
    level += 1
    for i in range(level):
        egg1 = Egg(egg1_img, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 0)
        egg_group.add(egg1)
        egg2 = Egg(egg2_img, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 1)
        egg_group.add(egg2)
        egg3 = Egg(egg3_img, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 2)
        egg_group.add(egg3)
        egg4 = Egg(egg4_img, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 3)
        egg_group.add(egg4)


start_new_level()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    my_player.draw()
    egg_group.update()
    egg_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
