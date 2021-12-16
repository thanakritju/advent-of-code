import pytest

from aoc2021.day15.path import lowest_cost


def test_lowest_cost():
    puzzle_input = open("aoc2021/day15/sample.txt", "r")
    content = puzzle_input.read()

    actual = lowest_cost(content)

    assert actual == 40


@pytest.mark.puzzle
def test_lowest_cost_for_puzzle():
    puzzle_input = open("aoc2021/day15/input.txt", "r")
    content = puzzle_input.read()

    actual = lowest_cost(content)

    assert actual == 720


def test_lowest_cost_5times():
    puzzle_input = open("aoc2021/day15/sample.txt", "r")
    content = puzzle_input.read()

    actual = lowest_cost(content, 5)

    assert actual == 315


@pytest.mark.puzzle
def test_lowest_cost_5timesfor_puzzle():
    puzzle_input = open("aoc2021/day15/input.txt", "r")
    content = puzzle_input.read()

    actual = lowest_cost(content, 5)

    assert actual == 3025
