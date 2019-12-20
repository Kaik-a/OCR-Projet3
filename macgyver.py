"""This module is set to implement MacGyver inside the maze"""
from operator import add
from config import MACGYVER_PICTURE
from maze import Maze


class MacGyver:
    """This class is set to represent our hero, macguyver, his methods and
     attributes. """
    def __init__(self):
        self.position = (0, 0)
        self.item_count = 0
        self.picture = MACGYVER_PICTURE

    def move(self, direction: str, maze: Maze):
        """This methods gives the ability to MacGyver to move inside the maze.

        Args:
            direction: the direction where MacGyver is trying to move
            maze: the maze from where MacGyver is trying to escape
        """

        def set_position(try_move: tuple):
            """If try_move is in accepted paths, we define the new position of
            McaGyver"""
            new_position = tuple(map(add, self.position, try_move))
            if new_position in maze.path:
                self.position = new_position

        if direction == 'up':
            move = (0, -1)
        elif direction == 'down':
            move = (0, 1)
        elif direction == 'left':
            move = (-1, 0)
        elif direction == 'right':
            move = (1, 0)

        set_position(move)

    def get_items(self, maze: Maze):
        """When MacGyver arrives in a new position, we verify if there's not an
        item on it

        Args:
            maze: the maze from where MacGyver is trying to escape
        """
        if self.position in maze.items:
            self.item_count += 1
            maze.items.remove(self.position)
