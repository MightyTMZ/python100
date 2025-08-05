from ..reverse_string import reverse_string
import pytest

test_reverse_string_array = [
    ("A", "A"),
    ("", ""),
    ("ABC", "CBA"),
    ("abcdefghi", "ihgfedcba"),
    ("racecar", "racecar")
]


@pytest.mark.parametrize("string, reversed", test_reverse_string_array)
def test_reverse_string(string, reversed):
    assert reverse_string(string) == reversed