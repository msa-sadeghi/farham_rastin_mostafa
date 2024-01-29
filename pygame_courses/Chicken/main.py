from constants import *
from player import Player
from egg import Egg
import random
clock = pygame.time.Clock()
FPS = 60
level = 0

target_egg_image = ""
target_egg_type = ""
target_egg_image_rect = ""

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

def draw():
    pygame.draw.rect(screen, (245,13,210), (0,100, SCREEN_WIDTH, SCREEN_HEIGHT - 200), 4)
    screen.blit(target_egg_image, target_egg_image_rect)
    # TODO  display scoreboard  : score,   lives,   level number,  warps number

def choose_new_target():
    global target_egg_image, target_egg_type,target_egg_image_rect
    target_egg = random.choice(egg_group.sprites())
    target_egg_image = target_egg.image
    target_egg_image_rect = target_egg_image.get_rect(bottom = 100, centerx = SCREEN_WIDTH/2)
    target_egg_type = target_egg.type
    
choose_new_target()  


def check_collisions():
    collided_egg = pygame.sprite.spritecollideany(my_player, egg_group)
    if collided_egg:
        if collided_egg.type == target_egg_type:
            collided_egg.remove(egg_group)
            if len(egg_group) != 0:
                choose_new_target() 
            else:
                start_new_level()
                my_player.reset()
                
        else:
            my_player.reset()
            # decrease the lives


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    check_collisions()
    draw()
    my_player.move()
    my_player.draw()
    egg_group.update()
    egg_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
