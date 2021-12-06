import pytest

from aoc2021.day6.lanternfish import get_lanternfish


@pytest.mark.parametrize(
    "test_fish,days,expected_fish",
    [
        ([3, 4, 3, 1, 2], 18, 26),
        ([3, 4, 3, 1, 2], 80, 5934),
        ([3, 4, 3, 1, 2], 17, 22),
        ([3, 4, 3, 1, 2], 256, 26984457539),
    ]
)
def test_get_lanternfish(test_fish, days, expected_fish):
    actual = get_lanternfish(test_fish, days)

    assert actual == expected_fish


@pytest.mark.puzzle
def test_get_lanternfish_for_puzzle():
    puzzle_input = open("aoc2021/day6/input.txt", "r")
    content = list(map(int, puzzle_input.read().split(",")))

    actual = get_lanternfish(content, 80)

    assert actual == 360610

    actual = get_lanternfish(content, 256)

    assert actual == 1631629590423
