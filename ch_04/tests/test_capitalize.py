from ..capitalize import capitalize
import pytest

test_capitalize_array = [
    (["this", "is", "a", "title"], ["is", "a"], ["This", "is", "a", "Title"]),
    (["only"], [], ["Only"]),
    (["only"], ["only"], ["only"]),
    ([], [], []),
    (["multiple", "words", "here"], ["words"], ["Multiple", "words", "Here"]),
    (["hello", "world"], ["world"], ["Hello", "world"]),
    (["hello", "world"], ["hello", "world"], ["hello", "world"]),
    (["😊", "smile"], ["😊"], ["😊", "Smile"]),
    (["你好", "世界"], ["世界"], ["你好", "世界"]),
]

@pytest.mark.parametrize("words, ignorable, expected", test_capitalize_array)
def test_capitalize(words, ignorable, expected):
    assert capitalize(words, ignorable) == expected
