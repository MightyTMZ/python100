from ..checksum import calc_checksum
import pytest

@pytest.mark.parametrize("n, expected", [
    ("11111", 5),
    ("111111", 1),
    ("1111111", 8),
    ("87654321", 0)
])
def test_checksum(n, expected):
    assert calc_checksum(n) == expected