"""
Main File.
Start program
Contains constant values
"""
import pygame
import sys
import start
from tools import create_image as create

COLORS = {"Background": pygame.Color('#231445'), "Player": pygame.Color('#8A6DCE'),
          "Platform": pygame.Color('#6339C4'), "Stair": pygame.Color('#492A8F')}

CAPTIONS = {"Start": 'Platformer | Start screen',
            "Game": 'Platformer | Game screen. Score: ',
            "New Game": 'Platformer | Create new game'}

SIZES = {"Player": (30, 30), "Platform": (100, 20), "Stair": (20, 100), "Icon": (20, 20), "Screen": (700, 700)}

IMAGES = {"Player": create(SIZES["Player"], COLORS["Player"]),
          "Platform": create(SIZES["Platform"], COLORS["Platform"]),
          "Stair": create(SIZES["Stair"], COLORS["Stair"]),
          "Icon": create(SIZES["Icon"], COLORS["Player"])}

FPS = 60


def main():
    """
    Main method.
    Start program
    """
    start.main()


if __name__ == '__main__':
    sys.exit(main())
