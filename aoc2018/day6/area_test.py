import pytest

from area import biggest_area, area_within_distance


def test_biggest_area():
    test_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]

    actual = biggest_area(test_input)

    assert actual == 17


@pytest.mark.puzzle
def test_biggest_area_for_puzzle_input():
    puzzle_input = open("aoc2018/day6/coordinates.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = biggest_area(content)

    assert actual == 5941


@pytest.mark.puzzle
def test_area_within_distance_for_puzzle_input():
    puzzle_input = open("aoc2018/day6/coordinates.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = area_within_distance(content, 10000)

    assert actual == 40244
