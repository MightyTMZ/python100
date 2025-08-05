from ..fibonacci import fib_rec, fib_iterative
import pytest

def fibonacci_test_array(): 
    return [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (14, 377),
        (15, 610),
    ]

@pytest.mark.parametrize("n, expected", fibonacci_test_array())
def test_fib_rec(n, expected):
    assert fib_rec(n) == expected

@pytest.mark.parametrize("n, expected", fibonacci_test_array())
def test_fib_iterative(n, expected):
    assert fib_iterative(n) == expected