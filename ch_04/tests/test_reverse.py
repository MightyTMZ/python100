import pytest
from ..reverse_string import reverse 

test_reverse_string_array = [
    ("abc", "cba"),
    ("x", "x"),
    ("", ""),
    ("madam", "madam"),
    ("a b c", "c b a"),
    ("  abc  ", "  cba  "),
    ("a   b", "b   a"),
    ("he@llo!", "!oll@eh"),
    ("AbCd", "dCbA"),
    ("12345", "54321"),
    ("你好世界", "界世好你"),
    ("😊👍", "👍😊"),
]


@pytest.mark.parametrize("n, expected", test_reverse_string_array)
def test_reverse_string(n, expected):
    assert reverse(n) == expected
