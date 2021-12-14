import pytest

from aoc2021.day13.fold import fold, print_fold


def test_fold():
    puzzle_input = open("aoc2021/day13/sample.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = fold(content, 1)

    assert actual == 17


@pytest.mark.puzzle
def test_fold_for_puzzle():
    puzzle_input = open("aoc2021/day13/input.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = fold(content, 1)

    assert actual == 735


@pytest.mark.puzzle
def test_print_fold_for_puzzle():
    puzzle_input = open("aoc2021/day13/input.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = print_fold(content, 12)

    assert actual == True
