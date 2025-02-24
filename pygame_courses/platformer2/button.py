import pygame

class Button:
    def __init__(self, img, x,y):
        self.image = img
        self.rect = self.image.get_rect(topleft=(x,y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        click = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                click = True

        return click

