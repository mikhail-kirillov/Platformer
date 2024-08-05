"""
Start File.
Open start screen
"""
import pygame
import sys
import game
from tools import Custom_Group
from button import Button
from main import COLORS, CAPTIONS, IMAGES, SIZES, FPS

PLAY_BUTTON_TEXT = 'Play'
PLAY_BUTTON_CORDS = (SIZES["Screen"][0] // 10 * 4 + (SIZES["Screen"][0] // 50), SIZES["Screen"][1] // 10 * 4)

EXIT_BUTTON_TEXT = 'Exit'
EXIT_BUTTON_CORDS = (SIZES["Screen"][0] - (SIZES["Screen"][0] // 10), SIZES["Screen"][1] - (SIZES["Screen"][1] // 10))

FONT_SIZE = 70
running = True
game_screen_open = False


def terminate():
    """
    Terminate method.
    Exit from program
    """
    sys.exit(pygame.quit())


def main():
    """
    Main method.
    View start screen
    """
    global running, game_screen_open

    pygame.init()
    pygame.display.set_caption(CAPTIONS["Start"])
    pygame.display.set_icon(IMAGES["Icon"])
    screen = pygame.display.set_mode(SIZES["Screen"])

    buttons = Custom_Group()
    buttons.add(Button(PLAY_BUTTON_TEXT, COLORS["Player"], game.main, FONT_SIZE, PLAY_BUTTON_CORDS))
    buttons.add(Button(EXIT_BUTTON_TEXT, COLORS["Stair"], terminate, FONT_SIZE // 3, EXIT_BUTTON_CORDS))

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons.handle_event(event)
        else:
            if not running or game_screen_open:
                break
        screen.fill(COLORS["Background"])
        buttons.draw(screen)
        buttons.update()
        pygame.display.flip()
        clock.tick(FPS)
    if not game_screen_open:
        pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
