"""File to launch in order to play MacGyver's maze game."""

from os import chdir
from time import sleep

import pygame
import pygame.locals

from config import ITEM_TO_WIN, WINDOW_SIZE, MACGYVER_PICTURE, WINDOW_TITLE
from model.level import Level
from view.maze_view import create_maze_view
from view.item_count_display import display_item_count

chdir('..')


def main():
    """Launch the game."""
    pygame.init()  # pylint: disable=maybe-no-member
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    icon = pygame.image.load(MACGYVER_PICTURE)
    pygame.display.set_icon(icon)

    pygame.display.set_caption(WINDOW_TITLE)

    level = Level()
    showdown = ''

    while 1:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            # pylint: disable=maybe-no-member
            if event.type == pygame.locals.QUIT:
                return
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_RIGHT:
                    level.macgyver.move('right', level.maze)
                elif event.key == pygame.locals.K_LEFT:
                    level.macgyver.move('left', level.maze)
                elif event.key == pygame.locals.K_DOWN:
                    level.macgyver.move('down', level.maze)
                elif event.key == pygame.locals.K_UP:
                    level.macgyver.move('up', level.maze)

            if showdown:
                return

            if level.macgyver.position == level.guardian.position:
                level.result(level.macgyver.item_count == ITEM_TO_WIN)
                showdown = 'done'

            create_maze_view(level.maze, window)

            window.blit(level.guardian.picture, level.guardian.position)
            window.blit(level.macgyver.picture, level.macgyver.position)

            display_item_count(window, level)

            pygame.display.flip()


if __name__ == "__main__":
    main()
    sleep(5)
