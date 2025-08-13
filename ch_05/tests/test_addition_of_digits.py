from ..addition_of_digits import list_add
import pytest

test_list_add_array = [
    ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
    ([0, 5, 7], [3, 2, 1], [3, 7, 8]),
    ([9, 8, 1], [1, 2, 3], [1, 1, 0, 4]),
    ([4, 0, 6], [5, 9, 2], [9, 9, 8]),
    ([7, 7, 7], [2, 2, 2], [9, 9, 9]),
    ([3, 4, 5], [6, 0, 1], [9, 4, 6]),
]


@pytest.mark.parametrize("a1, a2, expected", test_list_add_array)
def test_list_add(a1, a2, expected):
    assert list_add(a1, a2) == expected
