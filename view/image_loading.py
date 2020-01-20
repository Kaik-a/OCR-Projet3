"""function available to load images"""

import pygame
from config import SPRITE_SIZE


def load_image(image_file):
    try:
        image = pygame.transform.scale(pygame.image.load(image_file).convert(),
                                       (SPRITE_SIZE, SPRITE_SIZE))
    except pygame.error as message:
        print('Image at', image_file, 'unreachable')
        raise SystemExit(message)

    return image


def resize(sprite):
    try:
        sized_sprite = pygame.transform.scale(sprite,
                                              (SPRITE_SIZE, SPRITE_SIZE))

    except pygame.error as message:
        raise SystemExit(message)

    return sized_sprite

