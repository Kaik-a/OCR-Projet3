"""Abstract class for movable objects in the game."""

from pygame import sprite, image

from view.image_loading import load_image


class GameObject(sprite.Sprite):
    def __init__(self, picture: image, position: tuple):
        super(GameObject, self).__init__()
        self.position = position
        self.picture = load_image(picture)
