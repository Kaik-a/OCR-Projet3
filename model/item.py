"""Class representing items."""

import pygame


class Item(pygame.sprite.Sprite):
    """Items need to be picked up by macgyver in order to go out the maze."""
    def __init__(self, position, picture=None):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.picture = picture
