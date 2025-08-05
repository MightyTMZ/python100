from ..related_numbers import calc_friends
import pytest


@pytest.mark.parametrize("max, friends", [
    (250, {220: 284}),
    (300, {220: 284, 284: 220}),
    (2000, {220: 284, 284: 220, 1184: 1210, 1210: 1184}),
])
def test_calc_friends(max, friends):
    assert calc_friends(max) == friends