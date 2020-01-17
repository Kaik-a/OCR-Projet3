"""
Class representing the guardian inside the maze. It is not possible to
MacGyver to go through the exit if he doesn't have the three items hidden inside
the maze
"""

import pygame
from model.macgyver import MacGyver
from view.image_loading import load_image
from config import GUARDIAN_PICTURE


class Guardian(pygame.sprite.Sprite):
    """The guardian is here to protect the exit of the maze."""
    def __init__(self, position: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.picture = load_image(GUARDIAN_PICTURE)
        self.position = position

    @staticmethod
    def block_exit(macgyver: MacGyver):
        """
        If MacGyver get all items from maze he can sleep the guardian and go
        through exit, otherwise the guardian knock him out
        """
        if macgyver.item_count == 3:
            return "victory"
        return "fail"
