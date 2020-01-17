"""
This class is set to generate the maze from a file
"""
import pygame
from random import choice
from model.item import Item
from view.image_loading import load_image
from config import ETHER_PICTURE, SPRITE_SIZE, SYRINGE_PICTURE, TUBE_PICTURE


class Maze(pygame.sprite.Sprite):
    """This class reprensents the maze in the game. """

    def __init__(self, file):
        pygame.sprite.Sprite.__init__(self)
        self.wall = []
        self.path = []
        self.start = (0, 0)
        self.guardian = (0, 0)
        self.finish = (0, 0)
        self.items = []
        self.generate_maze(file)
        while len(self.items) < 3:
            self.item_at_random_location()

    def generate_maze(self, file):
        """This method allows us to create a maze from a file located in mazes's
        directory.

        Args:
            file: file containing maze structure's

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
                for sprite in line:
                    if sprite != '\n':
                        if sprite == 's':
                            self.start = (x, y)
                            self.path.append((x, y))
                        elif sprite == '0':
                            self.path.append((x, y))
                        elif sprite == 'w':
                            self.wall.append((x, y))
                        elif sprite == 'g':
                            self.guardian = (x, y)
                        elif sprite == 'f':
                            self.finish = (x, y)
                    x += SPRITE_SIZE
                x = 0
                y += SPRITE_SIZE

    def item_at_random_location(self):
        """This method is set to find a random location for the three items. """

        item_pictures = [ETHER_PICTURE, SYRINGE_PICTURE, TUBE_PICTURE]

        item_location = choice(self.path)
        # we avoid start and guardian location
        if (item_location in self.guardian or
                item_location in self.start):
            self.item_at_random_location()
        else:
            if self.items:
                # we avoid other item position
                for item in self.items:
                    if item_location in item.position:
                        self.item_at_random_location()
                self.items.append(Item(item_location))
            else:
                self.items.append(Item(item_location))

        # we load an image for each item in list
        for item in self.items:
            item.picture = load_image(item_pictures.pop())
