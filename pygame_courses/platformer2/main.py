from config import *
from character import Character
clock = pygame.time.Clock()
pygame.init()
player = Character("player", 100, 300, 60, 10)
moving_left, moving_right, jumped = (False, False, False)
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
    
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
    
    
    screen.fill((0,0,0))       
    player.draw(screen)  
    player.move(moving_left, moving_right)
    player.animation()     
    pygame.display.update()
    clock.tick(FPS)