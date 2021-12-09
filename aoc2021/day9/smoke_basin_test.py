import pytest

from aoc2021.day9.smoke_basin import count_low_points


def test_count_low_points():
    puzzle_input = open("aoc2021/day9/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = count_low_points(content)

    assert actual == 15


@pytest.mark.puzzle
def test_count_low_points_for_puzzle():
    puzzle_input = open("aoc2021/day9/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = count_low_points(content)

    assert actual == 498
