"""This module is set to implement MacGyver inside the maze."""
from operator import add
import pygame
from config import MACGYVER_PICTURE, SPRITE_SIZE
from view.image_loading import load_image
from model.maze import Maze


class MacGyver(pygame.sprite.Sprite):
    """
    This class is set to represent our hero, macguyver, his methods and
    attributes.
    """

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.item_count = 0
        self.picture = load_image(MACGYVER_PICTURE)

    def move(self, direction: str, maze: Maze):
        """
        This methods gives the ability to MacGyver to move inside the maze.

        Args:
            direction: the direction where MacGyver is trying to move
            maze: the maze from where MacGyver is trying to escape
        """

        move = (0, 0)

        def set_position(try_move: tuple):
            """
            If try_move is in accepted paths, we define the new position of
            McaGyver.
            """
            new_position = tuple(map(add, self.position, try_move))
            if (new_position in maze.path
                    or new_position == maze.guardian
                    or new_position in maze.finish):
                self.position = new_position

        def get_items():
            """
            When MacGyver arrives in a new position, we verify if there's
            not an item on it.
            """
            for item in maze.items:
                if self.position == item.position:
                    self.item_count += 1
                    maze.items.remove(item)

        if direction == 'up':
            move = (0, -SPRITE_SIZE)
        elif direction == 'down':
            move = (0, SPRITE_SIZE)
        elif direction == 'left':
            move = (-SPRITE_SIZE, 0)
        elif direction == 'right':
            move = (SPRITE_SIZE, 0)

        set_position(move)
        get_items()
