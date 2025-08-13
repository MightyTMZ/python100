from ..add_one_to_array import add_one
import pytest


@pytest.mark.parametrize("input_digits, expected", [
        ([1, 2, 3], [1, 2, 4]),
        ([0], [1]),
        ([5], [6]),
        ([1, 0, 0], [1, 0, 1]),
        ([1, 2, 9], [1, 3, 0]),
        ([9], [1, 0]),
        ([1, 9], [2, 0]),
        ([1, 9, 9], [2, 0, 0]),
        ([9, 9], [1, 0, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),   
        ([9, 9, 9, 9], [1, 0, 0, 0, 0]),
        ([0, 0, 9], [0, 1, 0]),
        ([0, 9, 9], [1, 0, 0]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 9, 0]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 2]),
])
def test_add_one(input_digits, expected):
    assert add_one(input_digits) == expected