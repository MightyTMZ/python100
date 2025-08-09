from ..number_palindromes import is_number_palindrome
import pytest


test_is_number_palindrome_array = [
    (12321, True),
    (123321, True),
    (56765, True),
    (567765, True),
    (1111111, True),
    (342873247, False),
    (1, True),
    (2, True),
    (8, True),
    (9, True),
    (10, False),
    (11, True),
    (33, True), 
    (43, False), 
]

@pytest.mark.parametrize("n, expected", test_is_number_palindrome_array)
def test_is_number_palindrome(n, expected):
    assert is_number_palindrome(n) == expected