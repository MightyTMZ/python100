from ..contains_all import contains_all
import pytest

test_contains_all_cases = [
    ([x for x in range(10)], [7, 2], True),
    ([x for x in range(10)], [11, 9], False),
    ([x for x in range(10)], [1, 4], True),
    ([x for x in range(10)], [10, 7], False),
    ([x for x in range(10)], [13, 9], False),
    ([x for x in range(10)], [6, 19], False),
    ([x for x in range(10)], [20, 7], False),
    ([x for x in range(10)], [18, 2], False),
    ([x for x in range(10)], [8, 2], True),
    ([x for x in range(10)], [12, 5], False),
    ([x for x in range(10)], [15, 2], False),
    ([x for x in range(10)], [15, 9], False),
    ([x for x in range(10)], [16, 3], False),
    ([x for x in range(10)], [12, 2], False),
    ([x for x in range(10)], [1, 2], True),
    ([x for x in range(10)], [6, 6], True),
    ([x for x in range(10)], [0, 9, 1, 2, 3, 4, 5], True),
]

@pytest.mark.parametrize("values, search_values, contain_all", test_contains_all_cases)
def test_contains_all(values, search_values, contain_all):
    assert contains_all(values, search_values) == contain_all