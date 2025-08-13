from ..palindrome import is_palindrome
import pytest

test_is_palindrome_list = [
    ([], True),
    ([""], True),
    (["a"], True),
    (["a", "b", "a"], True),
    (["a", "b", "c"], False),
    (["r", "a", "c", "e", "c", "a", "r"], True),
    (["1", "2", "3", "2", "1"], True),
    (["1", "2", "3", "4", "5"], False),
    (["hello", "world", "hello"], True),
]

@pytest.mark.parametrize("arr, is_palindrome_arr", test_is_palindrome_list)
def test_is_palindrome(arr, is_palindrome_arr):
    assert is_palindrome(arr) == is_palindrome_arr