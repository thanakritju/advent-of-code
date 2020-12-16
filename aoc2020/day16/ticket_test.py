import pytest

from aoc2020.day16.ticket import *


def test_get_error_rate():
    puzzle_input = open("aoc2020/day16/sample.txt", "r")
    content = puzzle_input.read()

    actual = get_error_rate(content)

    assert actual == 71


def test_get_multiply():
    puzzle_input = open("aoc2020/day16/sample2.txt", "r")
    content = puzzle_input.read()

    actual = get_multiply(content)

    assert actual == 1716


def test_get_error_rate_for_puzzle_input():
    puzzle_input = open("aoc2020/day16/input.txt", "r")
    content = puzzle_input.read()

    actual = get_error_rate(content)

    assert actual == 20231

    actual = get_multiply(content)

    assert actual == 1940065747861
