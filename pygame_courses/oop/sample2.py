import pygame
pygame.init()
clo = pygame.time.Clock()
class Wolf:
    def __init__(self,name, age, x,y, image, sound):
        self.name = name
        self.age = age
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.speed = 5
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    def draw(self):
        screen.blit(self.image, self.rect)


img1 = pygame.image.load("w1.png")
sound1 = pygame.mixer.Sound("w1.mp3")
wolf1 = Wolf("peter", 10, 100,100,img1, sound1)

img2 = pygame.image.load("w2.png")
sound2 = pygame.mixer.Sound("w2.mp3")
wolf2 = Wolf("martin", 6, 200,200, img2, sound2)





screen = pygame.display.set_mode((400,400))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    wolf1.draw()
    wolf1.move()
    wolf2.draw()
    wolf2.move()
    pygame.display.update()
    clo.tick(60)
