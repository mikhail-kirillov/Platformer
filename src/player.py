"""
Player file.
Contains Player class
"""
import pygame

from tools import Entity
from main import IMAGES, SIZES


class Player(Entity):
    """
    Player class. Main character and him functions
    """

    def __init__(self, size, pos, image, *groups):
        super().__init__(size, pos, image, *groups)
        self.image = IMAGES["Player"]
        self.rect = self.image.get_rect()
        self.rect.x = SIZES["Screen"][0] // 2
        self.rect.y = SIZES["Screen"][1] // 2
        self.score = 0

    def update(self, platform):
        """
        Player update. His moving
        :param platform: is colliding with this?
        """
        if not pygame.sprite.spritecollideany(self, platform):
            self.rect = self.rect.move(0, 1)
        if not (0 <= self.rect.y <= SIZES['Screen'][1]):
            self.score = 0
            self.rect.x = SIZES["Screen"][0] // 2
            self.rect.y = SIZES["Screen"][1] // 2
        if not (0 <= self.rect.x <= SIZES['Screen'][0]):
            self.score = 0
            self.rect.x = SIZES["Screen"][0] // 2
            self.rect.y = SIZES["Screen"][1] // 2

    def handle_event(self, event):
        """
        Moving by keys
        :param event: is this need event?
        """
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect = self.rect.move(-1, 0)
            self.score += 1
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect = self.rect.move(1, 0)
            self.score += 1
        if event is not None and event.key == pygame.K_SPACE:
            self.rect = self.rect.move(0, -30)
