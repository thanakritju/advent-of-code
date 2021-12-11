import pytest

from aoc2021.day11.octopus import count_flashes, when_to_flash


def test_count_flashes():
    puzzle_input = open("aoc2021/day11/sample.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_flashes(content, 10)

    assert actual == 204

    actual = count_flashes(content, 100)

    assert actual == 1656


@pytest.mark.puzzle
def test_count_flashes_for_puzzle():
    puzzle_input = open("aoc2021/day11/input.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_flashes(content, 100)

    assert actual == 1732


def test_when_to_flash():
    puzzle_input = open("aoc2021/day11/sample.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = when_to_flash(content)

    assert actual == 195


@pytest.mark.puzzle
def test_when_to_flash_for_puzzle():
    puzzle_input = open("aoc2021/day11/input.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = when_to_flash(content)

    assert actual == 290
