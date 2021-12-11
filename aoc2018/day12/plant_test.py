import pytest

from aoc2018.day12.plant import count_plants, count_plants_v2


def test_count_plants():
    puzzle_input = open("aoc2018/day12/sample.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_plants(content, 20)

    assert actual == 325


@pytest.mark.puzzle
def test_count_plants_for_puzzle():
    puzzle_input = open("aoc2018/day12/input.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_plants(content, 20)

    assert actual == 3903


@pytest.mark.puzzle
def test_count_plants_for_puzzle_part2():
    puzzle_input = open("aoc2018/day12/input.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_plants_v2(content, 50000000000)

    assert actual == 3450000002268
