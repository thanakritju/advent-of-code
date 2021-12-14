import pytest

from aoc2021.day14.polymerization import polymerize, count_polymerization


def test_count_polymerization():
    puzzle_input = open("aoc2021/day14/sample.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_polymerization(content, 10)

    assert actual == 1588


@pytest.mark.puzzle
def test_count_polymerization_10steps_for_puzzle():
    puzzle_input = open("aoc2021/day14/input.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_polymerization(content, 10)

    assert actual == 2447


@pytest.mark.puzzle
def test_count_polymerization_40steps_for_puzzle():
    puzzle_input = open("aoc2021/day14/input.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_polymerization(content, 40)

    assert actual == 3018019237563
