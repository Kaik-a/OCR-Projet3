"""In order to play the game, a level is created taking in parameters an
instance of a maze and a macgyver"""

from macgyver import MacGyver
from maze import Maze
from guardian import Guardian


class Level:
    def __init__(self, guardian: Guardian, macgyver: MacGyver, maze: Maze):
        self.guardian = guardian
        self.macgyver = macgyver
        self.maze = maze

    def victory(self):
        pass

    def fail(self):
        pass


