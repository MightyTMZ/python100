from ..well_formed_braces import check_braces
import pytest

test_check_braces_array = [
    ("", True),
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("({[]})", True),
    ("({[)]})", False),
    ("(", False),
    (")", False),
    ("([{}])", True),
    ("[(])", False),
    ("{[()()]}", True),
    ("{[(])}", False),
    ("{[", False),
    ("}]", False),
]


@pytest.mark.parametrize("text, expected", test_check_braces_array)
def test_check_braces(text, expected):
    assert check_braces(text) == expected
