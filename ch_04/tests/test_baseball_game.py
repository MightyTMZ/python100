from ..baseball_game import baseball_game
import pytest

@pytest.mark.parametrize("inning, half, first, second, third, balls, strikes, home, away, expected", [
    # No runners, no balls or strikes, start of inning
    (1, "top", False, False, False, 0, 0, 0, 0, 
     "Top of the 1st inning. There are 0 balls and 0 strikes. There are no runners on base. Score — Home: 0, Away: 0."),

    # One runner on first, some balls and strikes
    (3, "bottom", True, False, False, 2, 1, 5, 3,
     "Bottom of the 3rd inning. There are 2 balls and 1 strike. There is runner on first. Score — Home: 5, Away: 3."),

    # Runners on first and second, multiple balls and strikes
    (5, "top", True, True, False, 3, 2, 4, 4,
     "Top of the 5th inning. There are 3 balls and 2 strikes. There are runners on first, second. Score — Home: 4, Away: 4."),

    # Bases loaded, 1 ball and 0 strikes
    (7, "bottom", True, True, True, 1, 0, 8, 7,
     "Bottom of the 7th inning. There are 1 ball and 0 strikes. There are runners on first, second, third. Score — Home: 8, Away: 7."),

    # Runner only on third base, no balls or strikes
    (9, "top", False, False, True, 0, 0, 10, 9,
     "Top of the 9th inning. There are 0 balls and 0 strikes. There is runner on third. Score — Home: 10, Away: 9."),

    # No runners, 1 ball and 1 strike, 2nd inning bottom half
    (2, "bottom", False, False, False, 1, 1, 2, 3,
     "Bottom of the 2nd inning. There are 1 ball and 1 strike. There are no runners on base. Score — Home: 2, Away: 3."),

    # Runners on second and third, 0 balls 2 strikes
    (4, "top", False, True, True, 0, 2, 6, 6,
     "Top of the 4th inning. There are 0 balls and 2 strikes. There are runners on second, third. Score — Home: 6, Away: 6."),

    # Only one runner on second base, 3 balls 0 strikes
    (6, "bottom", False, True, False, 3, 0, 1, 0,
     "Bottom of the 6th inning. There are 3 balls and 0 strikes. There is runner on second. Score — Home: 1, Away: 0."),

    # Multiple innings with higher numbers (13th inning)
    (13, "top", True, False, True, 2, 2, 9, 10,
     "Top of the 13th inning. There are 2 balls and 2 strikes. There are runners on first, third. Score — Home: 9, Away: 10."),

    # Edge case: 11th inning (checks ordinal 'th' suffix)
    (11, "bottom", False, False, False, 0, 0, 0, 1,
     "Bottom of the 11th inning. There are 0 balls and 0 strikes. There are no runners on base. Score — Home: 0, Away: 1."),

    # 2nd inning top, runner on all bases, no balls/strikes
    (2, "top", True, True, True, 0, 0, 3, 2,
     "Top of the 2nd inning. There are 0 balls and 0 strikes. There are runners on first, second, third. Score — Home: 3, Away: 2."),

    # 21st inning bottom, no runners, 3 balls and 1 strike
    (21, "bottom", False, False, False, 3, 1, 7, 8,
     "Bottom of the 21st inning. There are 3 balls and 1 strike. There are no runners on base. Score — Home: 7, Away: 8."),
])
def test_baseball_game(inning, half, first, second, third, balls, strikes, home, away, expected):
    assert baseball_game(inning, half, first, second, third, balls, strikes, home, away) == expected
