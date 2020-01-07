"""File to launch in order to play MacGyver's maze game."""

import pygame
from pygame.locals import *
from Model.level import Level
from View.maze_view import create_maze_view
from config import WINDOW_SIZE, MACGYVER_PICTURE, WINDOW_TITLE


def main():
    """Launch the game."""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    icon = pygame.image.load(MACGYVER_PICTURE)
    pygame.display.set_icon(icon)

    pygame.display.set_caption(WINDOW_TITLE)

    level = Level()

    playing = True

    while True:
        while playing:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    playing = False
                    principal_loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        level.macgyver.move('right')
                    elif event.key == K_LEFT:
                        level.macgyver.move('left')
                    elif event.key == K_DOWN:
                        level.macgyver.move('down')
                    elif event.key == K_UP:
                        level.macgyver.move('up')

                create_maze_view(level.maze, window)
                window.blit(level.macgyver.picture, level.macgyver.position)

                pygame.display.flip()

                if level.macgyver.position == level.guardian.position:
                    showdown = level.guardian.block_exit(level.macgyver)
                    level.result(showdown)


if __name__ == "__main__":
    main()
