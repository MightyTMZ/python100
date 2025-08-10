from ..tennis_score import tennis_score
import pytest

test_tennis_scores_array = [
    # Basic scoring (0 to 3 points each)
    ("0:0", "Tom", "Eric", "Love Love"),
    ("0:1", "Tom", "Eric", "Love Fifteen"),
    ("0:2", "Tom", "Eric", "Love Thirty"),
    ("0:3", "Tom", "Eric", "Love Forty"),
    ("1:0", "Tom", "Eric", "Fifteen Love"),
    ("1:1", "Tom", "Eric", "Fifteen Fifteen"),
    ("1:2", "Tom", "Eric", "Fifteen Thirty"),
    ("1:3", "Tom", "Eric", "Fifteen Forty"),
    ("2:0", "Tom", "Eric", "Thirty Love"),
    ("2:1", "Tom", "Eric", "Thirty Fifteen"),
    ("2:2", "Tom", "Eric", "Thirty Thirty"),
    ("2:3", "Tom", "Eric", "Thirty Forty"),
    ("3:0", "Tom", "Eric", "Forty Love"),
    ("3:1", "Tom", "Eric", "Forty Fifteen"),
    ("3:2", "Tom", "Eric", "Forty Thirty"),
    ("3:3", "Tom", "Eric", "Deuce"),

    # Game won before deuce
    ("4:0", "Tom", "Eric", "Game Tom"),
    ("0:4", "Tom", "Eric", "Game Eric"),
    ("4:1", "Tom", "Eric", "Game Tom"),
    ("1:4", "Tom", "Eric", "Game Eric"),
    ("4:2", "Tom", "Eric", "Game Tom"),
    ("2:4", "Tom", "Eric", "Game Eric"),
    
    # Deuce and Advantage cases
    ("3:3", "Tom", "Eric", "Deuce"),
    ("4:4", "Tom", "Eric", "Deuce"),
    ("4:3", "Tom", "Eric", "Advantage Tom"),
    ("3:4", "Tom", "Eric", "Advantage Eric"),
    ("5:4", "Tom", "Eric", "Advantage Tom"),
    ("4:5", "Tom", "Eric", "Advantage Eric"),
    ("6:4", "Tom", "Eric", "Game Tom"),
    ("4:6", "Tom", "Eric", "Game Eric"),
    ("7:5", "Tom", "Eric", "Game Tom"),
    ("5:7", "Tom", "Eric", "Game Eric"),
    
    # Extended Deuce situations
    ("6:6", "Tom", "Eric", "Deuce"),
    ("7:7", "Tom", "Eric", "Deuce"),
    ("8:7", "Tom", "Eric", "Advantage Tom"),
    ("7:8", "Tom", "Eric", "Advantage Eric"),
    ("9:7", "Tom", "Eric", "Game Tom"),
    ("7:9", "Tom", "Eric", "Game Eric"),
    ("141:139", "Tom", "Eric", "Game Tom"),
    ("139:141", "Tom", "Eric", "Game Eric"),
    ("139:140", "Tom", "Eric", "Advantage Eric"),
    ("140:140", "Tom", "Eric", "Deuce"),
    ("141:140", "Tom", "Eric", "Advantage Tom"),
]

@pytest.mark.parametrize("score, p1, p2, expected_score", test_tennis_scores_array)
def test_tennis_score(score, p1, p2, expected_score):
    assert tennis_score(score, p1, p2) == expected_score
