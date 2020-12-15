import pytest

from aoc2020.day15.memory import *


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1,3,2", 1),
        ("2,1,3", 10),
        ("1,2,3", 27),
        ("0,3,6", 436),
        ("2,3,1", 78),
        ("3,2,1", 438),
        ("3,1,2", 1836),
    ]
)
def test_get_spoken_number(test_input, expected):
    actual = get_spoken_number(test_input, 2020)

    assert actual == expected


@pytest.mark.puzzle
def test_get_spoken_number_for_puzzle_input():
    puzzle_input = open("aoc2020/day15/input.txt", "r")
    content = puzzle_input.read()

    actual = get_spoken_number(content, 2020)

    assert actual == 240

    actual = get_spoken_number(content, 30000000)

    assert actual == 505
