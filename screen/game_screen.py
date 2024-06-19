import pygame
from utils.config import *
from utils.execute_game import execute_game
from utils.buttons import draw_back_button

pygame.init()


def game_screen():
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for title, info in game_files.items():
                    rect = tile_rects[list(game_files.keys()).index(title)]
                    if rect.collidepoint(mouse_pos):
                        execute_game(info["archivo"])
                        break
                if back_button_rect.collidepoint(mouse_pos):
                    return
        screen.blit(background_img, (0, 0))

        for title, info in game_files.items():
            rect = tile_rects[list(game_files.keys()).index(title)]

            imagen_mosaico = pygame.image.load(info["imagen_mosaico"]).convert_alpha()
            imagen_mosaico_original = pygame.transform.scale(imagen_mosaico, (225, 145))

            zoom_scale = 1.1 if rect.collidepoint(mouse_pos) else 1.0
            imagen_mosaico_zoom = pygame.transform.scale(
                imagen_mosaico, (int(230 * zoom_scale), int(150 * zoom_scale))
            )

            marco_scale = 1.1 if rect.collidepoint(mouse_pos) else 1.0
            marco_img_scaled = pygame.transform.scale(
                marco_img,
                (int(rect.width * marco_scale), int(rect.height * marco_scale)),
            )

            screen.blit(
                imagen_mosaico_zoom,
                (
                    rect.x
                    + 10
                    - (
                        imagen_mosaico_zoom.get_width()
                        - imagen_mosaico_original.get_width()
                    )
                    // 2,
                    rect.y
                    + 10
                    - (
                        imagen_mosaico_zoom.get_height()
                        - imagen_mosaico_original.get_height()
                    )
                    // 2,
                ),
            )

            screen.blit(
                marco_img_scaled,
                (
                    rect.x + (rect.width - marco_img_scaled.get_width()) // 2,
                    rect.y + (rect.height - marco_img_scaled.get_height()) // 2,
                ),
            )
            font_size = 20 if rect.collidepoint(mouse_pos) else 18

            font = pygame.font.Font(font_patch, font_size)
            text = font.render(title, True, BLACK)
            top = 5 if rect.collidepoint(mouse_pos) else 10
            text_rect = text.get_rect(center=(rect.centerx, rect.top + top))
            screen.blit(text, text_rect)

        back_button_rect = draw_back_button()

        pygame.display.flip()

    pygame.quit()
