from ..cross_sum import calc_sum_of_digits
import pytest

@pytest.mark.parametrize("num, sum", [
    (48234, 21),
    (1234567, 28),
    (1234, 10),
    (12345, 15),
    (123456, 21),
])
def test_calc_sum_of_digits(num, sum):
    assert calc_sum_of_digits(num) == sum