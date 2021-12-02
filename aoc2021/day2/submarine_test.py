import pytest

from aoc2021.day2.submarine import get_multiplication_of_coordinate, get_multiplication_of_coordinate_with_aim


def test_get_multiplication_of_coordinate():
    test_input = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    actual = get_multiplication_of_coordinate(test_input)

    assert actual == 150


@pytest.mark.puzzle
def test_get_multiplication_of_coordinate_for_puzzle():
    puzzle_input = open("aoc2021/day2/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_multiplication_of_coordinate(content)

    assert actual == 2036120


def test_get_multiplication_of_coordinate_with_aim():
    test_input = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    actual = get_multiplication_of_coordinate_with_aim(test_input)

    assert actual == 900


@pytest.mark.puzzle
def test_get_multiplication_of_coordinate_with_aim_for_puzzle():
    puzzle_input = open("aoc2021/day2/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_multiplication_of_coordinate_with_aim(content)

    assert actual == 2015547716
