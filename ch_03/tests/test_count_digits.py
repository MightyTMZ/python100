from ..count_digits import count_digits
import pytest

@pytest.mark.parametrize(('n, expected'), [
    (12345, 5),
    (1, 1),
    (1234, 4),
    (129, 3),
    (987654321, 9),
    (45435, 5),
    (67, 2),
])
def test_count_digits(n, expected):
    assert count_digits(n) == expected