from ..perfect_numbers import calc_perfect_numbers
import pytest


@pytest.mark.parametrize(
    "n, expected", [(100, [6, 28]), (1000, [6, 28, 496]), (10000, [6, 28, 496, 8128])]
)
def test_calc_perfect_number(n, expected):
    assert calc_perfect_numbers(n) == expected

