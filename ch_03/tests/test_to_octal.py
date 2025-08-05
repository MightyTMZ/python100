from ..conversions import to_octal
import pytest

test_to_octal_array = [
    (329, "511"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "10"),
    (9, "11"),
    (64, "100"),
    (512, "1000"),
    (513, "1001"),
]


@pytest.mark.parametrize("num, oct", test_to_octal_array)
def test_to_octal(num, oct):
    assert to_octal(num) == oct
