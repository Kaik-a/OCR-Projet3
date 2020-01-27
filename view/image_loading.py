"""function available to load images"""

import pygame
from config import SPRITE_SIZE


def load_image(image_file: str):
    """function to load an image for pygame

    :param image_file:  path of the image to load
    """
    try:
        image = resize(pygame.image.load(image_file).convert())
    except pygame.error as message:   # pylint: disable=no-member
        print('Image at', image_file, 'unreachable')
        raise SystemExit(message)

    return image


def resize(sprite: pygame.image):
    """function to resize an image using SPRITE_SIZE

    :param sprite: Image to resize
    """
    try:
        sized_sprite = pygame.transform.scale(sprite,
                                              (SPRITE_SIZE, SPRITE_SIZE))

    except pygame.error as message:  # pylint: disable=no-member
        raise SystemExit(message)

    return sized_sprite
