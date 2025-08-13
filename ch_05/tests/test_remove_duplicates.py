from ..remove_duplicates import remove_duplicates
import pytest


test_remove_duplicates_array = [
    ([1, 1, 2], [1, 2]),
    ([3, 4, 4], [3, 4]),
    ([5, 5, 5], [5]),
    ([2, 3, 2], [2, 3]),
    ([9, 8, 9], [9, 8]),
    [[7, 7, 8], [7, 8]],
]

@pytest.mark.parametrize("arr_with_dup, no_dup_arr", test_remove_duplicates_array)
def test_remove_duplicates(arr_with_dup, no_dup_arr):
    assert remove_duplicates(arr_with_dup) == no_dup_arr