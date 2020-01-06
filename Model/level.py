"""In order to play the game, a level is created taking in parameters an
instance of a maze and a macgyver"""

from Model.macgyver import MacGyver
from Model.maze import Maze
from Model.guardian import Guardian
from config import DEFAULT_FILE, RIP_PICTURE


class Level:
    def __init__(self):
        self.maze = Maze(DEFAULT_FILE)
        self.guardian = Guardian(self.maze.guardian)
        self.macgyver = MacGyver(self.maze.start)

    def result(self, showdown: str):
        if showdown == 'victory':
            self.macgyver.position = self.maze.finish
            self.guardian.picture = RIP_PICTURE
            print("You're finally out from the maze!!! Gratz!!!")
        elif showdown == 'fail':
            print("You died...")



