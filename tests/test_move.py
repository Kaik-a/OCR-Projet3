"""test for macgyver's method move. """

from model.macgyver import MacGyver
from tests.fixture import fixture
from config import SPRITE_SIZE, MACGYVER_PICTURE

fixture()


def test_move():
    from unittest import mock
    with mock.patch('model.maze') as mock:
        maze = mock.return_value
        maze.path = [(0, 0),
                     (SPRITE_SIZE, 0),
                     (0, SPRITE_SIZE),
                     (SPRITE_SIZE, SPRITE_SIZE)]

        macgyver = MacGyver(position=(0, 0), picture=MACGYVER_PICTURE)

        macgyver.move('right', maze)

        assert macgyver.position == (SPRITE_SIZE, 0)

        macgyver.move('left', maze)

        assert macgyver.position == (0, 0)

        macgyver.move('down', maze)

        assert macgyver.position == (0, SPRITE_SIZE)

        macgyver.move('up', maze)

        assert macgyver.position == (0, 0)

        macgyver.move('up', maze)

        assert macgyver.position == (0, 0)
