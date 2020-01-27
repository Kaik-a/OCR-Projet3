"""method to display the item count on the window"""
import pygame

from config import SPRITE_SIZE, WINDOW_SIZE
from model.level import Level


def display_item_count(window: pygame.display, level: Level):
    """Make of visual of how many items as been picked up

    :param window: Window where item count display
    :param level: Level where MacGyver is collecting item
    """
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', SPRITE_SIZE // 2)
    if level.macgyver.item_count < 3:
        text = font.render(f'Item: {level.macgyver.item_count}/3', True, green)
    else:
        text = font.render('Syringe ready', True, green)
    window.blit(text, (0, WINDOW_SIZE - SPRITE_SIZE // 2))
