import pygame
from main import IMAGES, SIZES


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = IMAGES['Platform']
        self.rect = pygame.Rect((pos[0], pos[1]), SIZES['Platform'])
        self.x = pos[0]
        self.y = pos[1]
        self.speed = 1
        self.move = True

    def update(self):
        if self.rect.x + self.rect.width >= SIZES['Screen'][0]:
            self.move = False
        elif self.rect.x <= 0:
            self.move = True
        if self.move:
            self.rect = self.rect.move(self.speed, 0)
        else:
            self.rect = self.rect.move(-self.speed, 0)
