"""Test for Maze method generate_maze."""

from model.maze import Maze
from config import DEFAULT_FILE
from tests.fixture import fixture

fixture()


def test_generate_maze():
    maze = Maze(DEFAULT_FILE)

    assert len(maze.path) == 111

    assert len(maze.wall) == 112


