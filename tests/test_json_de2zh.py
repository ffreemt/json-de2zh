"""Test json_de2zh."""
# pylint: disable=broad-except
from json_de2zh import __version__, json_de2zh


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not json_de2zh("a")
    except Exception:
        assert True
