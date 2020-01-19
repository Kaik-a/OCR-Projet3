"""test image loading"""

import pytest
from view.image_loading import load_image


def test_unknown_image():
    with pytest.raises(SystemExit) as excinfo:
        load_image('ressource/Images/unknown_file.png')
    assert "Couldn't open" in str(excinfo.value)


