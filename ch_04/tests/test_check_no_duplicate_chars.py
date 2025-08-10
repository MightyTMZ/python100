from ..no_duplicate_chars import check_no_duplicate_chars
import pytest

test_no_duplicate_chars_array = [
    ("abc", True),
    ("aA", False),
    ("", True),
    ("abcdefg", True),
    ("abcdea", False),
    ("12345", True),
    ("112345", False),
    ("AaBbCc", False),
    ("a b c", False),
    ("abc def", True),
    ("😊👍", True),
    ("😊😊", False),
    ("你好世界", True),
    ("你好你", False),
]

@pytest.mark.parametrize("text, expected", test_no_duplicate_chars_array)
def test_check_no_duplicate_chars(text, expected):
    assert check_no_duplicate_chars(text) == expected
