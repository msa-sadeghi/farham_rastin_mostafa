import pygame

from button import Button

WIDTH = 800
HEIGHT = 640
MAX_COLS = 150
ROWS = 16
SIDE_MARGIN = 300
LOWER_MARGIN = 100
clock = pygame.time.Clock()

TILE_SIZE = HEIGHT // ROWS


mountain_img = pygame.image.load("./assets/images/background/mountain.png")
pine1_img = pygame.image.load("./assets/images/background/pine1.png")
pine2_img = pygame.image.load("./assets/images/background/pine2.png")
sky_cloud_img = pygame.image.load("./assets/images/background/sky_cloud.png")

def draw_background():
    screen.blit(sky_cloud_img, (0,0))
    screen.blit(mountain_img, (0,HEIGHT - mountain_img.get_height() - 300))
    screen.blit(pine1_img, (0,HEIGHT - pine1_img.get_height() - 200))
    screen.blit(pine2_img, (0,HEIGHT - pine2_img.get_height() - 50))

tile_images = list()
for i in range(21):
    img = pygame.image.load(f"./assets/images/tile/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    tile_images.append(img)
col =0
row = 0
buttons_list = list()
for i in range(21):
    btn = Button(
        tile_images[i],
        WIDTH + col * 60 + 60,
        row * 60 + 60    
        )
    buttons_list.append(btn)
    col += 1
    if col == 3:
        row+= 1
        col = 0

FPS = 60
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_background()       
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + LOWER_MARGIN)) 
    for i in range(21):
        buttons_list[i].draw(screen)
    pygame.display.update()
    clock.tick(FPS)