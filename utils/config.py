import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Minijuegos")

background_img = pygame.image.load("assets/img/fondo.jpg").convert()
background_img = pygame.transform.scale(background_img, (800, 600))

marco_img = pygame.image.load("assets/img/marco.png").convert_alpha()
marco_img = pygame.transform.scale(marco_img, (240, 160))

tile_rects = [
    pygame.Rect(100, 100, 240, 160),
    pygame.Rect(500, 100, 240, 160),
    pygame.Rect(100, 400, 240, 160),
    pygame.Rect(500, 400, 240, 160),
]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (90, 90, 90)

font_patch = "assets/fonts/font_game.TTF"
font_title = pygame.font.Font(font_patch, 36)
font_text = pygame.font.Font(font_patch, 24)

username = ""
grade = 1
input_active = False
dropdown_active = False

game_files = {
    "Garden": {
        "archivo": "games/pydewvalley/code/main.py",
        "autor": "Nombre del Autor 1",
        "imagen_mosaico": "assets/img/minigame1.jpg",
    },
    "Juego 2": {
        "archivo": "game2.py",
        "autor": "Nombre del Autor 2",
        "imagen_mosaico": "assets/img/minigame.jpg",
    },
    "Juego 3": {
        "archivo": "game3.py",
        "autor": "Nombre del Autor 3",
        "imagen_mosaico": "assets/img/minigame.jpg",
    },
    "Juego 4": {
        "archivo": "game4.py",
        "autor": "Nombre del Autor 4",
        "imagen_mosaico": "assets/img/minigame.jpg",
    },
}
