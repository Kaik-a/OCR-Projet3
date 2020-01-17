"""File to launch in order to play MacGyver's maze game."""

from os import chdir
import pygame
from pygame.locals import *
from time import sleep
from model.level import Level
from view.maze_view import create_maze_view
from view.item_count_display import display_item_count
from config import WINDOW_SIZE, MACGYVER_PICTURE, WINDOW_TITLE, WIN_PICTURE, FAIL_PICTURE

chdir('..')

# TODO: Check python path for main and tests


def main():
    """Launch the game."""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    icon = pygame.image.load(MACGYVER_PICTURE)
    pygame.display.set_icon(icon)

    pygame.display.set_caption(WINDOW_TITLE)

    level = Level()
    showdown = ''

    while 1:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    level.macgyver.move('right', level.maze)
                elif event.key == K_LEFT:
                    level.macgyver.move('left', level.maze)
                elif event.key == K_DOWN:
                    level.macgyver.move('down', level.maze)
                elif event.key == K_UP:
                    level.macgyver.move('up', level.maze)

            if showdown:
                return

            if level.macgyver.position == level.guardian.position:
                showdown = level.guardian.block_exit(level.macgyver)
                level.result(showdown)

            create_maze_view(level.maze, window)

            window.blit(level.guardian.picture, level.guardian.position)
            window.blit(level.macgyver.picture, level.macgyver.position)

            display_item_count(window, level)

            pygame.display.flip()


if __name__ == "__main__":
    main()
    sleep(5)
