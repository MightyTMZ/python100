from ..joiner import join
import pytest

test_join_array = [
    (["hello", "world", "message"], "++=", "hello++=world++=message"),
    (["only"], "sep", "only"),
    ([], "sep", ""),
    (["a", "b", "c"], "", "abc"),
    (["", "", ""], "-", "--"),
    (["a", "", "b"], "|", "a||b"),
    (["x", "y"], "longdelimiter", "xlongdelimitery"),
    (["a", "b", "c"], "@#$", "a@#$b@#$c"),
    (["first", "second", "third"], " ", "first second third"),
    ([" a ", " b ", " c "], "-", " a - b - c "),
    (["1", "2", "3"], ",", "1,2,3"),
    (["你好", "世界"], "🌏", "你好🌏世界"),
    (["one", "two"], "😊", "one😊two"),
]

@pytest.mark.parametrize("values, delimitter, expected", test_join_array)
def test_join(values, delimitter, expected):
    assert join(values, delimitter) == expected
