from ..morse_code import to_morse_code
import pytest

test_morse_code_limited_array = [
    ("E", "."),                   # single supported letter
    ("O", "---"),
    ("S", "..."),
    ("T", "-"),
    ("W", ".--"),
    ("SOS", "... --- ..."),       # combination
    ("TEST", "- . ... -"),        # mix of supported letters
    ("WOW", ".-- --- .--"),
    ("SEE", "... . ."),
    ("TO", "- ---"),
    ("", ""),
]

@pytest.mark.parametrize("input_str, expected", test_morse_code_limited_array)
def test_string_to_morse_limited(input_str, expected):
    assert to_morse_code(input_str) == expected
