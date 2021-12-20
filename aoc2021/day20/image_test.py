import pytest

from aoc2021.day20.image import process


def test_process_magnitude():
    puzzle_input = open(f"aoc2021/day20/sample.txt", "r")
    content = puzzle_input.read()

    actual = process(content, 1)

    assert actual == 24

    actual = process(content, 2)

    assert actual == 35

    # actual = process(content, 50)

    # assert actual == 3351


@pytest.mark.puzzle
def test_process_for_puzzle():
    puzzle_input = open(f"aoc2021/day20/input.txt", "r")
    content = puzzle_input.read()

    actual = process(content, 2, True)

    assert actual == 5483

    actual = process(content, 50, True)

    assert actual == 5483
