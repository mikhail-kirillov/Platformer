"""
Game File.
Open game screen
"""
import pygame
import sys
from main import COLORS, CAPTIONS, IMAGES, SIZES, FPS
from player import Player
from tools import Custom_Group
from platform import Platform
from random import randint


def main():
    """
    Main method.
    View game screen, Processes the game
    """
    pygame.init()
    pygame.display.set_icon(IMAGES["Icon"])
    screen = pygame.display.set_mode(SIZES["Screen"])

    player_sprite = Custom_Group()
    player = Player(
        size=SIZES['Player'],
        pos=(SIZES['Screen'][0] // 2, SIZES['Screen'][1] // 2),
        image=IMAGES['Player']
        )
    player_sprite.add(player)

    pygame.display.set_caption(CAPTIONS["Game"] + str(player.score))

    platforms = Custom_Group()
    for _ in range(10):
        tmp = Platform(pos=(randint(0, SIZES['Screen'][0]), randint(0, SIZES['Screen'][1])))
        if (not pygame.sprite.spritecollideany(tmp, platforms)) \
                and \
                (0 <= tmp.rect.x <= SIZES['Screen'][0]
                 and
                 0 <= tmp.rect.y <= SIZES['Screen'][1]):
            platforms.add(tmp)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player_sprite.handle_event(event)
        player_sprite.handle_event(None)

        screen.fill(COLORS["Background"])

        platforms.draw(screen)
        platforms.update()
        player_sprite.draw(screen)
        player_sprite.update(platforms)

        pygame.display.flip()
        clock.tick(FPS)
        pygame.display.set_caption(CAPTIONS["Game"] + str(player.score))
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
