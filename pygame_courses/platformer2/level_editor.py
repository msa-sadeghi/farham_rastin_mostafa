import pygame

from button import Button

WIDTH = 800
HEIGHT = 640
MAX_COLS = 150
ROWS = 16
SIDE_MARGIN = 300
LOWER_MARGIN = 100
clock = pygame.time.Clock()
scroll = 0
scroll_left, scroll_right = (False, False)
TILE_SIZE = HEIGHT // ROWS
selected_tile = 0

mountain_img = pygame.image.load("./assets/images/background/mountain.png")
pine1_img = pygame.image.load("./assets/images/background/pine1.png")
pine2_img = pygame.image.load("./assets/images/background/pine2.png")
sky_cloud_img = pygame.image.load("./assets/images/background/sky_cloud.png")

def draw_background():
    width = sky_cloud_img.get_width()
    for i in range(4):
        screen.blit(sky_cloud_img, (i * width - scroll,0))
        screen.blit(mountain_img, (i * width - scroll,HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, (i * width - scroll,HEIGHT - pine1_img.get_height() - 200))
        screen.blit(pine2_img, (i * width - scroll,HEIGHT - pine2_img.get_height()))


def draw_lines():
    for i in range(ROWS + 1):
        pygame.draw.line(
            screen, "white",(0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE)
        )
    for i in range(MAX_COLS + 1):
        pygame.draw.line(
            screen, "white",(i * TILE_SIZE - scroll, 0), (i * TILE_SIZE - scroll, HEIGHT)
        )

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

world_data = []
r = [-1] * MAX_COLS
for i in range(ROWS):
    world_data.append(r)

def draw_world():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            screen.blit(tile_images[world_data[i][j]], (j * TILE_SIZE, i * TILE_SIZE))


FPS = 60
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
    draw_background()       
    draw_lines()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + LOWER_MARGIN)) 
    for i in range(21):
        if buttons_list[i].draw(screen):
            selected_tile = i
            


    pygame.draw.rect(screen, "red", buttons_list[selected_tile].rect, 3)
    if pygame.mouse.get_pressed()[0]:
        mouse_position = pygame.mouse.get_pos()
        col = (mouse_position[0] + scroll) // TILE_SIZE
        row = mouse_position[1] // TILE_SIZE
        world_data[row][col] = selected_tile



    if scroll_right:
        scroll += 5
    if scroll_left and scroll > 0:
        scroll -= 5
    pygame.display.update()
    clock.tick(FPS)