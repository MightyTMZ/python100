from ..list_min import list_min
import pytest

test_list_min_array = [
    ([7, 2, 1, 9, 7, 1], 1),
    ([11, 2, 33, 44, 55, 6, 7], 2),
    ([1, 2, 3, -7], -7),
]

@pytest.mark.parametrize("values, expected_min", test_list_min_array)
def test_list_min(values, expected_min):
    assert list_min(values) == expected_min

    