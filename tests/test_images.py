"""test image loading"""

from pytest import raises
from view.image_loading import load_image


def test_unknown_image():
    with raises(SystemExit) as excinfo:
        load_image('ressource/Images/unknown_file.png')
    assert "Couldn't open" in str(excinfo.value)


