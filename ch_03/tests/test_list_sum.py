from ..list_sum import list_sum
import pytest

test_list_sum_array = [
    ([1, 2, 3], 6),
    ([1, 2, 3, -7], -1),
    ([1, 2, 3, -7, 10], 9),
    ([1, 2, 3, -7, 10, 11], 20),
    ([1, 2, 3, -7, 10, 11, -100], -80),
]


@pytest.mark.parametrize("l, expected_sum", test_list_sum_array)
def test_list_sum(l, expected_sum):
    assert list_sum(l) == expected_sum