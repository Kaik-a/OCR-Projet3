"""In order to play the game, a level is created taking in parameters an
instance of a maze and a macgyver"""

import pygame
from model.macgyver import MacGyver
from model.maze import Maze
from model.guardian import Guardian
from view.image_loading import load_image
from config import DEFAULT_FILE, RIP_PICTURE


class Level:
    def __init__(self):
        self.maze = Maze(DEFAULT_FILE)
        self.guardian = Guardian(self.maze.guardian)
        self.macgyver = MacGyver(self.maze.start)

    def result(self, showdown: str):
        if showdown == 'victory':
            #self.macgyver.position = self.maze.finish
            self.guardian.picture = load_image(RIP_PICTURE)
            print("You're finally out from the maze!!! Gratz!!!")
        elif showdown == 'fail':
            print("You died...")



