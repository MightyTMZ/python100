from ..gcd import gcd
import pytest

@pytest.mark.parametrize("a, b, expected_gcd", [
    (42, 7, 7),
    (42, 14, 14),
    (8, 7, 1),
    (99, 7, 1),
])
def test_gcd(a, b, expected_gcd):
    assert gcd(a, b) == expected_gcd
