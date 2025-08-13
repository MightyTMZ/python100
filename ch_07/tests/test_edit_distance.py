from ..edit_distance import edit_distance
import pytest

test_edit_distance_cases = [
    ("", "", 0),
    ("a", "", 1),
    ("", "a", 1),
    ("kitten", "sitting", 3),
    ("flaw", "lawn", 2),
    ("intention", "execution", 5),
    ("Hello", "hello", 0),
    ("abc", "ABC", 0),
    ("abcdef", "azced", 3),
    ("", "abcdef", 6),
]

@pytest.mark.parametrize("str1, str2, expected", test_edit_distance_cases)
def test_edit_distance(str1, str2, expected):
    assert edit_distance(str1, str2) == expected
