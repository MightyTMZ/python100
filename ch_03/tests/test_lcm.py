from ..lcm import lcm_recursive, lcm_iterative
import pytest


test_lcm_array = [
    (42, 7, 42),
    (42, 14, 42),
    (8, 7, 56),
    (99, 7, 693),
]


@pytest.mark.parametrize("a, b, expected_lcm", test_lcm_array)
def test_lcm_recursive(a, b, expected_lcm):
    assert lcm_recursive(a, b) == expected_lcm


@pytest.mark.parametrize("a, b, expected_lcm", test_lcm_array)
def test_lcm_iterative(a, b, expected_lcm):
    assert lcm_iterative(a, b) == expected_lcm
