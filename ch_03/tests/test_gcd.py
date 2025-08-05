from ..gcd import gcd, gcd_iterative
import pytest


def test_gcd_array():
    return [
        (42, 7, 7),
        (42, 14, 14),
        (8, 7, 1),
        (99, 7, 1),
    ]


@pytest.mark.parametrize(
    "a, b, expected_gcd", test_gcd_array()
)
def test_gcd_recursive(a, b, expected_gcd):
    assert gcd(a, b) == expected_gcd


@pytest.mark.parametrize(
    "a, b, expected_gcd", test_gcd_array()
)
def test_gcd_iterative(a, b, expected_gcd):
    assert gcd_iterative(a, b) == expected_gcd
