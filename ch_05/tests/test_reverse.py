from ..list_reverse import reverse
from ..list_reverse_in_place import reverse_inplace
import pytest

test_reverse_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [3, 2, 1]),
    (['a', 'b', 'c'], ['c', 'b', 'a']),
    ([True, False, True], [True, False, True]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([1, 2, 3, 2, 1], [1, 2, 3, 2, 1]),
    ([10, 20, 30, 40], [40, 30, 20, 10]),
]


@pytest.mark.parametrize("a, reversed_a", test_reverse_cases)
def test_reverse_simple(a, reversed_a):
    assert reverse(a) == reversed_a


@pytest.mark.parametrize("a, reversed_a", test_reverse_cases)
def test_reverse_inplace(a, reversed_a):
    assert reverse_inplace(a) == reversed_a