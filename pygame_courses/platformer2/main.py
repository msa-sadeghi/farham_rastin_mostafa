from config import *
from character import Character
clock = pygame.time.Clock()

player = Character("player", 100, 300, 60, 10)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.draw(screen)       
    pygame.display.update()
    clock.tick(FPS)