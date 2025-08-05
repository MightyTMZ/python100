from ..power import is_power_of
import pytest

test_is_power_of_array = [
    (64, 2, True),
    (2, 1, False),
    (3, 3, True),
    (1, 1, True),
    (128, 8, False),
    (4096, 2, True),
    (8192, 16, False),
    (82, 9, False),
    (81, 9, True),
]

@pytest.mark.parametrize("m, n,  b", test_is_power_of_array)
def test_is_power_of(m, n, b):
    assert is_power_of(m, n) == b
