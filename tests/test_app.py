import pytest

from app import add, is_even


def test_add_simple():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


@pytest.mark.parametrize("value, expected", [
    (2, True),
    (3, False),
    (10, True),
])
def test_is_even(value, expected):
    assert is_even(value) == expected