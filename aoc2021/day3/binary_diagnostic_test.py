import pytest

from aoc2021.day3.binary_diagnostic import get_diagnostic, get_diagnostic_v2


def test_get_multiplication_of_coordinate():
    puzzle_input = open("aoc2021/day3/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_diagnostic(content)

    assert actual == 198


@pytest.mark.puzzle
def test_get_multiplication_of_coordinate_for_puzzle():
    puzzle_input = open("aoc2021/day3/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_diagnostic(content)

    assert actual == 3895776


def test_get_multiplication_of_coordinate():
    puzzle_input = open("aoc2021/day3/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_diagnostic_v2(content)

    assert actual == 230


@pytest.mark.puzzle
def test_get_multiplication_of_coordinate_for_puzzle():
    puzzle_input = open("aoc2021/day3/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_diagnostic_v2(content)

    assert actual == 7928162
