from ..power import is_power_of_2
import pytest

test_is_power_of_2_array = [
    (64, True),
    (2, True),
    (3, False),
    (31, False),
    (128, True),
    (4096, True),
    (8192, True),
    (8193, False),
    (65, False),
]

@pytest.mark.parametrize("num, b", test_is_power_of_2_array)
def test_is_power_of_2(num, b):
    assert is_power_of_2(num) == b
