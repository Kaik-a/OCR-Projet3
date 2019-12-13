"""This module is set to implement MacGyver inside the maze"""
import operator
import config


class MacGyver:
    """This class is set to represent our hero, macguyver, his methods and attributes. """
    def __init__(self, maze):
        self.position = (0, 0)
        self.item_count = 0
        self.picture = config.MACGYVER_PICTURE
        self.maze = maze

    def move(self, direction: str):
        """This methods gives the ability to MacGyver to move inside the maze.

        Args:
            direction: the direction where MacGyver is trying to move
        """
        new_position = (0, 0)

        if direction == 'up':
            move = (0, 1)
            new_position = tuple(map(operator.add, self.position, move))
            if new_position not in self.maze.wall:
                self.position = new_position
            # TODO: implement the out of the box
        elif direction == 'down':
            pass
        elif direction == 'left':
            pass
        elif direction == 'right':
            pass
