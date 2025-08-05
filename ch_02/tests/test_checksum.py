from ..checksum import calc_checksum
import pytest

@pytest.mark.parametrize("n, expected", [
    ("11111", 5),
    ("111111", 1),
    ("1111111", 8),
    ("87654321", 0),
    ('12345678', 4),
])
def test_checksum(n, expected):
    assert calc_checksum(n) == expected

def test_calc_checksum_with_letters_as_wrong_input():
    with pytest.raises(ValueError) as excinfo:
        calc_checksum("ABC")

    assert "illegal chars" in str(excinfo.value)