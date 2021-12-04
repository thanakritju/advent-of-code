import pytest

from aoc2018.day9.marble_mania import get_high_score


@pytest.mark.parametrize(
    "players,last_marble_worth,high_score",
    [
        (9, 25, 32),
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
        (417, 71052, 37305),
    ]
)
def test_get_high_score(players, last_marble_worth, high_score):
    actual = get_high_score(players, last_marble_worth)

    assert actual == high_score
