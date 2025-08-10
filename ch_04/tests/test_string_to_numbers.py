from ..string_to_numbers import binary_to_decimal, hex_to_decimal
import pytest

@pytest.mark.parametrize("n, expected", [
    ("0", 0),
    ("1", 1),
    ("10", 2),
    ("101", 5),
    ("11111111", 255),
])
def test_binary_to_decimal(n, expected):
    assert binary_to_decimal(n) == expected


@pytest.mark.parametrize("n, expected", [
    ("0", 0),
    ("1", 1),
    ("A", 10),
    ("10", 16),
    ("FF", 255),
    ("1A3", 419),
])
def test_hex_to_decimal(n, expected):
    assert hex_to_decimal(n) == expected
