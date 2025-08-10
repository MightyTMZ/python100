from ..palindrome import is_palindrome
import pytest


test_is_palindrome_array = [
    ('racecar', True),
    ('ABCDCBA', True),
    ('Otto', True),
    ('ABCBX', False),
    ('ABCXcba', True),
    ('Tom', False),
    ('Eric', False),
    ('LeBron James', False),
    ('Corey Seager', False),
]

@pytest.mark.parametrize("n, expected", test_is_palindrome_array)
def test_is_palindrome(n, expected):
    assert is_palindrome(n) == expected