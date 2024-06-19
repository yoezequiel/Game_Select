import pygame
from utils.config import screen

back_button_img = pygame.image.load("assets/img/flecha.png").convert_alpha()
back_button_img = pygame.transform.scale(back_button_img, (40, 40))


def draw_back_button():
    back_button_rect = pygame.Rect(10, 10, 40, 40)
    screen.blit(back_button_img, back_button_rect.topleft)
    return back_button_rect
