"""
Tools File.
Contains useful classes and methods
"""
import pygame


class Entity(pygame.sprite.Sprite):
    """
    The entity class.
    Describes all the objects of the game
    """

    def __init__(self, size, pos, image, *groups):
        super().__init__(*groups)
        self.size = size
        self.pos = pos
        self.image = image

    def handle_event(self, event):
        """
        Method-stub
        :param event: event from the main loop
        """
        pass


def create_image(size, color):
    """
    Create image on surface
    :param size: surface and image size
    :param color: color to fill surface
    :return: image on surface
    """
    tmp = pygame.Surface(size)
    tmp.fill(color)
    return tmp


class Custom_Group(pygame.sprite.Group):
    """
    Custom Sprite Group with handle event
    """
    def handle_event(self, event):
        """
        Implements the method in sprites
        :param event: event from the main loop
        """
        for spr in self.sprites():
            spr.handle_event(event)
