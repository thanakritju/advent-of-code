import pytest

from aoc2021.day5.hydrothermal_venture import get_overlapped_points, get_overlapped_points_with_diagonal


def test_get_overlapped_points():
    puzzle_input = open("aoc2021/day5/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_overlapped_points(content)

    assert actual == 5


@pytest.mark.puzzle
def test_get_overlapped_points_for_puzzle():
    puzzle_input = open("aoc2021/day5/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_overlapped_points(content)

    assert actual == 6397


def test_get_overlapped_points_with_diagonal():
    puzzle_input = open("aoc2021/day5/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_overlapped_points_with_diagonal(content)

    assert actual == 12


@pytest.mark.puzzle
def test_get_overlapped_points_for_puzzle():
    puzzle_input = open("aoc2021/day5/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_overlapped_points_with_diagonal(content)

    assert actual == 22335
