from ..remove_duplicate_letters import remove_duplicates
import pytest

test_remove_duplicates_array = [
    ("banana", "ban"),
    ("", ""),
    ("aaaaa", "a"),
    ("abcabc", "abc"),
    ("112233", "123"),
    ("AaAaBbBb", "AaBb"),
    ("😊😊👍👍", "😊👍"),
    ("hello world", "helo wrd"),
    ("The quick brown fox", "The quickbrownfx"),
    ("1122!!@@##", "12!@#"),
]

@pytest.mark.parametrize("input_str, expected", test_remove_duplicates_array)
def test_remove_duplicates(input_str, expected):
    assert remove_duplicates(input_str) == expected
