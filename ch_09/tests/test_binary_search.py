from ..binary_search import binary_search
import pytest

test_binary_search_cases = [
    ([x for x in range(10)], 5, True),
    ([x for x in range(10)], -1, False),
    ([x for x in range(10)], 0, True),
    ([x for x in range(10)], -3, False),
    ([x for x in range(10)], 4, True),
    ([x for x in range(10)], 11, False),
    ([x for x in range(10)], 6, True),
    ([x for x in range(10)], -1, False),
    ([x for x in range(10)], 7, True),
    ([x for x in range(10)], -1, False),
    ([x for x in range(10)], 8, True),
    ([x for x in range(10)], -1, False),
    ([x for x in range(10)], 9, True),
    ([x for x in range(10)], -1, False),
    ([x for x in range(10)], 10.4, False),
    ([x for x in range(10)], -100, False),
    ([x for x in range(10)], 1, True),
    ([x for x in range(10)], -69, False),
    ([x for x in range(10)], 9, True),
    ([x for x in range(10)], 69, False),
    ([x for x in range(10)], 3, True),
    ([x for x in range(10)], -14, False),

]

@pytest.mark.parametrize("values, search_val, found", test_binary_search_cases)
def test_binary_search(values, search_val, found):
    assert binary_search(values, search_val) == found

    