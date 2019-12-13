import pygame


class Maze(pygame.sprite.Sprite):
    """This class reprensents the maze in the game. """
    def __init__(self, file):
        self.wall = []
        self.path = []
        self.start = (0, 0)
        self.finish = (15, 15)
        self.items = []
        self.generate_maze(file)

    def generate_maze(self, file):
        """This method allows us to create a maze from a file in mazes's directory. """

        x = 0
        y = 0

        with open(file, 'r') as f:
            for line in file:
                for sprite in line:
                    if sprite != '\n':
                        if sprite == 'd':
                            self.start = (x, y)
                        elif sprite == '0':
                            self.path.append((x, y))
                        elif sprite == 'm':
                            self.wall.append((x, y))
                        else:
                            self. finish = (x, y)
                    x += 1
                y += 1

    def item_at_random_location(self):
