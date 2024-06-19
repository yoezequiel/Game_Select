import pygame
import sqlite3
from database.db import create_db
from screen.game_screen import game_screen
from utils.config import *

pygame.init()


def draw_main_screen():
    screen.blit(background_img, (0, 0))
    text = font_title.render("Ingresa tu Nombre", True, DARK_GRAY)
    screen.blit(text, (150, 150))

    pygame.draw.rect(screen, BLACK, (300, 200, 200, 40), 2)
    text_surface = font_text.render(username, True, BLACK)
    screen.blit(text_surface, (310, 210))

    if input_active:
        pygame.draw.line(
            screen,
            BLACK,
            (310 + text_surface.get_width() + 5, 210),
            (310 + text_surface.get_width() + 5, 240),
        )

    pygame.draw.rect(screen, BLACK, (300, 280, 200, 40), 2)
    grade_text = font_text.render(f"Grado: {grade}", True, BLACK)
    screen.blit(grade_text, (310, 290))

    if dropdown_active:
        for i in range(1, 8):
            pygame.draw.rect(screen, GRAY, (300, 280 + i * 40, 200, 40), 0)
            grade_option_text = font_text.render(f"{i}", True, BLACK)
            screen.blit(grade_option_text, (310, 290 + i * 40))
            pygame.draw.rect(screen, BLACK, (300, 280 + i * 40, 200, 40), 2)
    else:
        pygame.draw.rect(screen, BLACK, (315, 400, 165, 50), 2)
        enter_text = font_text.render("Ingresar", True, BLACK)
        screen.blit(enter_text, (320, 415))

    pygame.display.flip()


def main():
    global username, grade, input_active, dropdown_active
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= event.pos[0] <= 500 and 200 <= event.pos[1] <= 240:
                    input_active = True
                    dropdown_active = False
                elif 300 <= event.pos[0] <= 500 and 280 <= event.pos[1] <= 320:
                    dropdown_active = not dropdown_active
                    input_active = False
                elif dropdown_active and 300 <= event.pos[0] <= 500:
                    for i in range(1, 8):
                        if 280 + i * 40 <= event.pos[1] <= 320 + i * 40:
                            grade = i
                            dropdown_active = False
                            break
                elif (
                    not dropdown_active
                    and 350 <= event.pos[0] <= 450
                    and 400 <= event.pos[1] <= 450
                ):
                    if username.strip():
                        conn = sqlite3.connect("database/users.db")
                        c = conn.cursor()
                        c.execute("SELECT * FROM users WHERE username = ?", (username,))
                        user = c.fetchone()
                        if not user:
                            c.execute(
                                "INSERT INTO users (username, grade) VALUES (?, ?)",
                                (username, grade),
                            )
                            conn.commit()
                        conn.close()
                        game_screen()
                    else:
                        print("El campo de nombre está vacío")
                else:
                    input_active = False
                    dropdown_active = False
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        draw_main_screen()

    pygame.quit()


if __name__ == "__main__":
    create_db()
    main()
