from ..anagram import is_anagram, is_anagram_with_no_spaces
import pytest

test_is_anagram_array = [
    ("listen", "silent", True),
    ("triangle", "integral", True),
    ("apple", "pale", False),
    ("Dormitory", "Dirty room", True),
    ("Conversation", "Voices rant on", True),
    ("hello", "billion", False),
    ("", "", True),
    ("a", "A", True),
    ("a ", "a", True),
    ("abc", "cba", True),
    ("abc", "abcc", False),
    ("School master", "The classroom", True),
    ("The eyes", "They see", True),
    ("The Morse Code", "Here come dots", True),
]

@pytest.mark.parametrize("a, b, expected", test_is_anagram_array)
def test_is_anagram(a, b, expected):
    assert is_anagram_with_no_spaces(a, b) == expected