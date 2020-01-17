"""In order to play the game, a level is created taking in parameters an
instance of a maze and a macgyver"""

from model.macgyver import MacGyver
from model.maze import Maze
from model.guardian import Guardian
from view.image_loading import load_image
from config import DEFAULT_FILE, RIP_PICTURE


class Level:
    """Main class of the game who permits to link maze, macgyver and guardian"""
    def __init__(self):
        self.maze = Maze(DEFAULT_FILE)
        self.guardian = Guardian(self.maze.guardian)
        self.macgyver = MacGyver(self.maze.start)

    def result(self, showdown: str):
        """If macgyver have all three items, showdown contain vitory he fails
        otherwise"""
        if showdown == 'victory':
            self.macgyver.position = self.maze.finish
            self.guardian.picture = load_image(RIP_PICTURE)
        elif showdown == 'fail':
            self.macgyver.picture = load_image(RIP_PICTURE)



