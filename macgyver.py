"""This module is set to implement MacGyver inside the maze"""
import operator
import config


class MacGyver:
    """This class is set to represent our hero, macguyver, his methods and
     attributes. """
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

        def set_position(try_move: tuple):
            """If try_move is in accepted paths, we define the new position of
            McaGyver"""
            new_position = tuple(map(operator.add, self.position, try_move))
            if new_position in self.maze.path:
                self.position = new_position

        if direction == 'up':
            move = (0, 1)
            set_position(move)
        elif direction == 'down':
            move = (0, -1)
            set_position(move)
        elif direction == 'left':
            move = (-1, 0)
            set_position(move)
        elif direction == 'right':
            move = (1, 0)
            set_position(move)
