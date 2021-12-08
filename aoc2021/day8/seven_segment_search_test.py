import pytest

from aoc2021.day8.seven_segment_search import search_seven_segment, get_sum_of_output


def test_search_seven_segment():
    puzzle_input = open("aoc2021/day8/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = search_seven_segment(content)

    assert actual == 26


@pytest.mark.puzzle
def test_search_seven_segment_for_puzzle():
    puzzle_input = open("aoc2021/day8/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = search_seven_segment(content)

    assert actual == 247


def test_get_sum_of_output():
    actual = get_sum_of_output(
        ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"])

    assert actual == 5353

    puzzle_input = open("aoc2021/day8/sample.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_sum_of_output(content)

    assert actual == 61229


@pytest.mark.puzzle
def test_get_sum_of_output_for_puzzle():
    puzzle_input = open("aoc2021/day8/input.txt", "r")
    content = list(map(str, puzzle_input.read().splitlines()))

    actual = get_sum_of_output(content)

    assert actual == 247
