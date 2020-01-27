"""
This class is set to generate the maze from a file
"""

from random import choice
from typing import List

from pygame import sprite

import config
from model.game_object import GameObject

item_pictures = [config.ETHER_PICTURE,
                 config.TUBE_PICTURE,
                 config.NEEDLE_PICTURE]


class Maze(sprite.Sprite):
    """This class reprensents the maze in the game. """

    def __init__(self, file: str):
        super(Maze, self).__init__()
        self.wall: List[tuple] = []
        self.path: List[tuple] = []
        self.start = (0, 0)
        self.guardian = (0, 0)
        self.finish = (0, 0)
        self.items: List[GameObject] = []
        self.generate_maze(file)
        while len(self.items) < config.ITEM_TO_WIN:
            self.item_at_random_location()

    def generate_maze(self, file: str):
        """This method allows us to create a maze from a file located in mazes's
        directory.

        :param file: file containing maze structure's

        In file:
            s: start
            w: wall
            0: path
            g: guardian
            f: finish
        """

        x = 0
        y = 0

        with open(file, 'r')as maze:
            for line in maze:
                for character in line:
                    if character != '\n':
                        if character == 's':
                            self.start = (x, y)
                            self.path.append((x, y))
                        elif character == '0':
                            self.path.append((x, y))
                        elif character == 'w':
                            self.wall.append((x, y))
                        elif character == 'g':
                            self.guardian = (x, y)
                        elif character == 'f':
                            self.finish = (x, y)
                    x += config.SPRITE_SIZE
                x = 0
                y += config.SPRITE_SIZE

    def item_at_random_location(self):
        """This method is set to find a random location for the three items."""

        item_location = choice(self.path)
        # we avoid start and guardian location
        if (item_location in self.guardian or
                item_location in self.start):
            self.item_at_random_location()
            return
        else:
            if self.items:
                # we avoid other items position
                for item in self.items:
                    if item_location in item.position:
                        self.item_at_random_location()
                        return
                self.items.append(GameObject
                                  (picture=item_pictures[len(self.items)],
                                   position=item_location))
            else:
                self.items.append(GameObject
                                  (picture=item_pictures[len(self.items)],
                                   position=item_location))
