from ..even_or_odd import is_odd, is_even
import pytest


@pytest.mark.parametrize("n, expected", [
    (1, False),
    (2, True), 
    (3, False),
    (4, True),
    (5, False),
    (6, True),
    (7, False),
    (8, True),
    (9, False),
    (10, True),
    (11, False),
    (12, True),
    (13, False),
    (14, True),
    (15, False),
    (16, True),
    (17, False),
    (18, True),
    (19, False),
    (20, True),
    (21, False),
    (22, True),
    (23, False),
    (24, True),
    (25, False),
])
def test_is_even(n, expected):
    assert is_even(n) == expected



@pytest.mark.parametrize("n, expected", [
    (1, True),
    (2, False),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, True),
    (10, False),
    (11, True),
    (12, False),
    (13, True),
    (14, False),
    (15, True),
    (16, False),
    (17, True),
    (18, False),
    (19, True),
    (20, False),
    (21, True),
    (22, False),
    (23, True),
    (24, False),
    (25, True),
])
def test_is_odd(n, expected):
    assert is_odd(n) == expected