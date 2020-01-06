"""File to launch in order to play MacGyver's maze game"""

from Model.level import Level
import pygame


def main():
    pygame.init()

    level = Level()

    while True:
        direction = input('Please enter a direction')
        level.macgyver.move(direction, level.maze)

        if level.macgyver.position == level.guardian.position:
            showdown = level.guardian.block_exit(level.macgyver)
            level.result(showdown)


if __name__ == "__main__":
    main()
