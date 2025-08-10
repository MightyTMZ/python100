from ..permutations import calc_permutations
import pytest


test_calc_permutations_array = [
        ("A", {"A"}),
        ("AA", {"AA"}),
        ("AB", {"AB", "BA"}),
        ("ABC", {"ABC", "ACB", "BAC", "BCA", "CAB", "CBA"}),
        ("AAC", {"ACA", "AAC", "CAA"}),
    ]


@pytest.mark.parametrize("n, expected", test_calc_permutations_array)
def test_calc_permutations(n, expected):
    assert calc_permutations(n) == expected
