"""In order to play the game, a level is created taking in parameters an
instance of a maze, a guardian and a macgyver"""

import config
from model.macgyver import MacGyver
from model.maze import Maze
from model.game_object import GameObject
from view.image_loading import load_image


class Level:
    """
    Main class of the game who permits to link maze, macgyver and guardian
    """
    def __init__(self):
        self.maze = Maze(file=config.DEFAULT_FILE)
        self.guardian = GameObject(picture=config.GUARDIAN_PICTURE,
                                   position=self.maze.guardian)
        self.macgyver = MacGyver(picture=config.MACGYVER_PICTURE,
                                 position=self.maze.start)

    def result(self, asleep_guardian: bool):
        """
        If macgyver have all three items, it's a vitory. He fails
        otherwise

        :param asleep_guardian: if macgyver have all items it's true
        """
        if asleep_guardian is True:
            self.macgyver.position = self.maze.finish
            self.guardian.picture = load_image(config.RIP_PICTURE)
        elif asleep_guardian is False:
            self.macgyver.picture = load_image(config.RIP_PICTURE)
