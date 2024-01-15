import random
import pygame
pygame.init()
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60

def paused():
    global running, score,dog_lives
    Game_over_text = my_font.render('Game over\nPress Enter to play again', True, (255,20,170))
    Game_over_rect = Game_over_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(Game_over_text, Game_over_rect)

    pygame.display.update()

    p = True
    while p:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    p = False
                    score = 0
                    dog_lives = 3
                if event.type == pygame.QUIT:
                    p = False
                    running = False




score = 0
dog_lives = 3

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

my_font = pygame.font.Font('assets/font.ttf',64)
welcome_text = my_font.render('Welcome To My Game', True, (255,20,170))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

score_text = my_font.render(f"Score:{score}", True, (10,170,230))
score_rect = score_text.get_rect(topleft=(0,0))

lives_text = my_font.render(f"lives:{dog_lives}", True, (10,170,230))
lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH,0))


dog_img = pygame.image.load("assets/dog.png")
dog_rect = dog_img.get_rect(bottom = SCREEN_HEIGHT, centerx = SCREEN_WIDTH/2)

bone_img = pygame.image.load("assets/bone.png")
bone_rect = bone_img.get_rect(top = 100, centerx = SCREEN_WIDTH/2)

# pygame.mixer.music.load("اسم فایل صدا")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.7)

pick_sound = pygame.mixer.Sound("assets/pick.wav")
# pick_sound.set_volume(0.9)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 3000:
        screen.blit(welcome_text, welcome_rect)
    else:
        keys = pygame.key.get_pressed()
        # حرکت دادن سگ به چهار طرف
        if keys[pygame.K_LEFT] and dog_rect.left >= 0:
            dog_rect.x -= 5

        if keys[pygame.K_RIGHT] and dog_rect.right <= SCREEN_WIDTH:
            dog_rect.x += 5
        if keys[pygame.K_UP] and dog_rect.top > 100:
            dog_rect.y -= 5

        if keys[pygame.K_DOWN] and dog_rect.bottom <= SCREEN_HEIGHT:
            dog_rect.y += 5


        bone_rect.y += 5
        if bone_rect.bottom >= SCREEN_HEIGHT:
            dog_lives -= 1
            bone_rect.center = (random.randint(32,SCREEN_WIDTH-32), 100-32)

        if dog_lives <= 0:
            paused()


        if dog_rect.colliderect(bone_rect):
            bone_rect.center = (random.randint(32,SCREEN_WIDTH-32), 100-32)
            score += 1
            pick_sound.play()

        score_text = my_font.render(f"Score:{score}", True, (10,170,230))
        lives_text = my_font.render(f"lives:{dog_lives}", True, (10,170,230))
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)
        screen.blit(dog_img, dog_rect)
        screen.blit(bone_img, bone_rect)
    
    
    pygame.display.update()
    clock.tick(FPS)