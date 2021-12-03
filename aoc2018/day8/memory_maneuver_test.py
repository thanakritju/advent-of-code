import pytest

from aoc2018.day8.memory_maneuver import get_sum_of_all_metadata_entries, get_sum_of_all_metadata_entries_v2


def test_get_multiplication_of_coordinate():
    puzzle_input = open("aoc2018/day8/sample.txt", "r")
    content = list(map(int, puzzle_input.read().split(" ")))

    actual = get_sum_of_all_metadata_entries(content)

    assert actual == 138


@pytest.mark.puzzle
def test_get_multiplication_of_coordinate_for_puzzle():
    puzzle_input = open("aoc2018/day8/input.txt", "r")
    content = list(map(int, puzzle_input.read().split(" ")))

    actual = get_sum_of_all_metadata_entries(content)

    assert actual == 44338


def test_get_multiplication_of_coordinate_v2():
    puzzle_input = open("aoc2018/day8/sample.txt", "r")
    content = list(map(int, puzzle_input.read().split(" ")))

    actual = get_sum_of_all_metadata_entries_v2(content)

    assert actual == 66


@pytest.mark.puzzle
def test_get_multiplication_of_coordinate_v2_for_puzzle():
    puzzle_input = open("aoc2018/day8/input.txt", "r")
    content = list(map(int, puzzle_input.read().split(" ")))

    actual = get_sum_of_all_metadata_entries_v2(content)

    assert actual == 2036120
