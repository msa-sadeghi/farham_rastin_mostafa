from config import *
from character import Character
clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
pygame.init()
player = Character("player", 100, 300, 60, 10)
moving_left, moving_right, jumped = (False, False, False)
bullet_shoot = False
grenade_shoot = False
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jumped = True
            if event.key == pygame.K_SPACE:
                bullet_shoot = True
            if event.key == pygame.K_g:
                grenade_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
            if event.key == pygame.K_SPACE:
                bullet_shoot = False
            if event.key == pygame.K_g:
                grenade_shoot = False
    
    if player.alive:
        if moving_left or moving_right:
            player.change_action("Run")
        else:
            player.change_action("Idle")
            
        if jumped and not player.in_air:
            player.gravity = -18
            player.in_air = True
        
        if player.in_air:
            player.change_action("Jump")
        if bullet_shoot:
            player.shoot("bullet", player_bullet_group)
        if grenade_shoot:
            player.shoot("grenade", grenade_group)
    
    screen.fill((0,0,0))       
    player.draw(screen)  
    player.move(moving_left, moving_right)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    grenade_group.update()
    grenade_group.draw(screen)
    player.animation()     
    pygame.display.update()
    clock.tick(FPS)