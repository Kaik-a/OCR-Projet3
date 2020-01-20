"""Class for game objects."""

from pygame import sprite, image

from view.image_loading import load_image


class GameObject(sprite.Sprite):
    """
    This class make a pattern for all game object which are representated in
    the maze
    """
    def __init__(self, picture: image, position: tuple):
        super(GameObject, self).__init__()
        self.position = position
        self.picture = load_image(picture)
