import pytest

from aoc2020.day17.game_of_life import get_all_actives
from aoc2020.day17.game_of_life2 import get_all_actives_4d


@pytest.mark.parametrize(
    "cycles,expected",
    [
        (1, 11),
        (2, 21),
        (0, 5),
        (6, 112),
    ]
)
def test_get_all_actives(cycles, expected):
    puzzle_input = open("aoc2020/day17/sample.txt", "r")
    content = puzzle_input.read()

    actual = get_all_actives(content, cycles)

    assert actual == expected


@pytest.mark.parametrize(
    "cycles,expected",
    [
        (1, 29),
        (2, 60),
        (0, 5),
        #(6, 848),
    ]
)
def test_get_all_actives_4d(cycles, expected):
    puzzle_input = open("aoc2020/day17/sample.txt", "r")
    content = puzzle_input.read()

    actual = get_all_actives_4d(content, cycles)

    assert actual == expected


@pytest.mark.puzzle
def test_get_all_actives_for_puzzle_input():
    puzzle_input = open("aoc2020/day17/input.txt", "r")
    content = puzzle_input.read()

    actual = get_all_actives(content)

    assert actual == 448

    actual = get_all_actives_4d(content)

    assert actual == 2400
