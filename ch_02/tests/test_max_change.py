from ..max_change_calculator import calc_max_possible_change
import pytest


@pytest.mark.parametrize("n, expected", [
    ([1], 1),
    ([1, 1], 2),
    ([1, 1, 1], 3),
    ([1, 4,], 1),
    ([1, 2, 3], 6),
    ([1, 2, 4], 7),
    ([1, 5,], 1),
    ([1, 6,], 1),
    ([1, 7,], 1),
    ([1 ,2, 3, 7], 13),
    ([1, 2, 3, 8], 6),

])
def test_max_change(n, expected):
    assert calc_max_possible_change(n) == expected