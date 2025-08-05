from ..armstrong_numbers import is_armstrong_number
import pytest

@pytest.mark.parametrize("n, expected", [
    (371, True),
    (153, True),
    (152, False),
])

def test_is_armstrong_number(n, expected):
    assert is_armstrong_number(n) == expected