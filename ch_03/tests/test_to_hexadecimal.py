from ..conversions import to_hexadecimal
import pytest

test_to_hexadecimal_array = [
    (329, "149"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "A"),
    (11, "B"),
    (12, "C"),
    (13, "D"),
    (14, "E"),
    (15, "F"),
    (64, "40"),
]


@pytest.mark.parametrize("num, oct", test_to_hexadecimal_array)
def test_to_hexadecimal(num, oct):
    assert to_hexadecimal(num) == oct


def test_to_hexadecimal_negative():
    with pytest.raises(ValueError, match="x has to be greater than or equal to 0"):
        to_hexadecimal(-1)