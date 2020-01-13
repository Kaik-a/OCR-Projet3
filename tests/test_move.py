"""test for macgyver's method move. """

from os import chdir
from unittest import mock
from model.macgyver import MacGyver
from tests.fixture import fixture

fixture()

with mock.patch('model.maze') as mock:
    maze = mock.return_value
    maze.path = [(20, 20), (20, 40), (20, 60)]

    macgyver = MacGyver((0, 0))

    macgyver.move('right', maze)

    assert macgyver.position == '(1, 1)'
