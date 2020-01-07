"""
Module to realize the display of the maze
"""
import pygame
from Model.maze import Maze
from config import SPRITE_SHEET


def create_maze_view(maze: Maze, window: pygame.display.set_mode()):
    """Make pygame visual for the maze."""
    sprite_sheet = pygame.image.load(SPRITE_SHEET)
    # load sprite image for walls
    sprite_sheet.set_clip(pygame.Rect(40, 0, 20, 20))
    wall_sprite = sprite_sheet.subsurface(sprite_sheet.get_clip())
    # load the sprite for goal
    sprite_sheet.set_clip(pygame.Rect(380, 0, 20, 20))
    finish_sprite = sprite_sheet.subsurface(sprite_sheet.get_clip())
    # load the sprite for normal floor
    sprite_sheet.set_clip(pygame.Rect(20, 0, 20, 20))
    path_sprite = sprite_sheet.subsurface(sprite_sheet.get_clip())

    for wall in maze.wall:
        window.blit(wall_sprite, wall)
    for path in maze.path:
        window.blit(path_sprite, path)
    for finish in maze.finish:
        window.blit(finish_sprite, finish)
