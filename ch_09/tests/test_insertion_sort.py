from ..insertion_sort import insertion_sort
import random

def test_insertion_sort():
    values = [37, 82, 15, 94, 61, 23, 48, 5, 76, 59, 2, 88, 41, 13, 69]
    expected = [2, 5, 13, 15, 23, 37, 41, 48, 59, 61, 69, 76, 82, 88, 94]

    insertion_sort(values) # no return, modifies the original list

    assert values == expected
