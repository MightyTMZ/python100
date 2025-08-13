from ..maximum_profit import max_revenue_optimized
import pytest

test_max_revenue_array = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2, 3, 4, 5], 4),
    ([5, 5, 5, 5], 0),
    ([2, 4, 1], 2),
    ([3, 2, 6, 1, 4], 4),
]

@pytest.mark.parametrize("prices, expected", test_max_revenue_array)
def test_max_revenue_optimized(prices, expected):
    assert max_revenue_optimized(prices) == expected