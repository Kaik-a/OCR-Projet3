"""Item's class."""

import pygame


class Item(pygame.sprite.Sprite):
    def __init__(self, position, picture=None):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.picture = picture
