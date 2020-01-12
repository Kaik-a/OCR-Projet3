"""
Class representing the guardian inside the maze. It is not possible to
MacGyver to go through the exit if he doesn't have the three items hidden inside
the maze
"""

import pygame
from Model.macgyver import MacGyver
from config import GUARDIAN_PICTURE


class Guardian(pygame.sprite.Sprite):
    """The guardian is here to protect the exit of the maze."""
    def __init__(self, position: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.picture = pygame.transform.scale(pygame.image.
                                              load(GUARDIAN_PICTURE).convert(),
                                              (20, 20))
        self.position = position

    @staticmethod
    def block_exit(macgyver: MacGyver):
        """
        If MacGyver go all items from maze he can sleep the guardian and go
        through exit, otherwise the guardian knock him out
        """
        if macgyver.item_count == 3:
            print("What's happening to me!? Hugh... \n "
                  "The guardian felt asleep")
            return "victory"

        print("You'll never go out!!! \n "
              "The guardian knocks out MacGyver's head")
        return "fail"
