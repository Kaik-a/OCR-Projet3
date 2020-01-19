"""test guardian method block_exit"""

from tests.fixture import fixture
from model.level import Level

fixture()

level = Level()


def test_victory():
    level.macgyver.item_count = 3
    result = level.guardian.block_exit(level.macgyver)

    assert result == 'victory'


def test_fail():
    level.macgyver.item_count = 2
    result = level.guardian.block_exit(level.macgyver)

    assert result == 'fail'
