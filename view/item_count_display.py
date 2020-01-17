"""method to display the item count on the window"""
import pygame
from config import SPRITE_SIZE, WINDOW_SIZE


def display_item_count(window, level):
    green = (0, 255, 0)
    font = pygame.font.Font('freesansbold.ttf', SPRITE_SIZE // 2)
    text = font.render(f'item: {level.macgyver.item_count}', True, green)
    window.blit(text, (0, WINDOW_SIZE - SPRITE_SIZE // 2))
