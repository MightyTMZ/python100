from ..conversions import to_binary
import pytest

test_to_binary_array = [
    (0, "0"),
    (1, "1"),
    (7, "111"),
    (8, "1000"),
    (31, "11111"),
    (32, "100000"),
]


@pytest.mark.parametrize("num, bin", test_to_binary_array)
def test_to_binary(num, bin):
    assert to_binary(num) == bin

def test_to_binary_negative():
    with pytest.raises(ValueError, match="x has to be greater than or equal to 0"):
        to_binary(-1)
