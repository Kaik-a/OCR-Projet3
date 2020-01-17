"""test for maze's method item_at_random_location"""

from config import DEFAULT_FILE
from model.maze import Maze
from tests.fixture import fixture

fixture()


def test_item_at_random_location():
    maze = Maze(DEFAULT_FILE)

    assert len(maze.items) == 3

    for item in maze.items:
        assert item.position not in maze.start
        assert item.position not in maze.guardian
