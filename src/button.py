"""
Button File.
Contains button class
"""
import pygame

import start
from tools import create_image as create
from main import COLORS


class Button(pygame.sprite.Sprite):
    """
    Class Button.
    Describes all text buttons
    """

    def __init__(self, text, color, method, font_size, cords, *groups):
        super().__init__(*groups)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(self.text, True, color)
        self.rect = self.text.get_rect()
        self.method = method
        self.image = create(self.rect.size, COLORS["Background"])
        self.image.blit(self.text, self.rect)
        self.rect = self.image.get_rect()
        self.rect.x = cords[0]
        self.rect.y = cords[1]

    def handle_event(self, event):
        """
        Method-stub
        :param event: event from the main loop
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos[0], event.pos[1]):
            start.running = False
            start.game_screen_open = True
            self.method()
