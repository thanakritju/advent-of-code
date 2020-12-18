import pytest

from aoc2020.day18.math import *


@pytest.mark.parametrize(
    "expressions, expected",
    [
        ('2 * 3', 6),
        ('2 + 3', 5),
        ('2 + 3 * 5', 25),
        ('2 * 3 + (4 * 5)', 26),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
    ]
)
def test_calculate(expressions, expected):
    actual = calculate(expressions)

    assert actual == expected


@pytest.mark.parametrize(
    "expressions, expected",
    [
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('2 + 3 * 5', 25),
        ('2 * 3 + (4 * 5)', 46),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
    ]
)
def test_calculate(expressions, expected):
    actual = calculate(expressions, True)

    assert actual == expected


@pytest.mark.puzzle
def test_calculate_for_puzzle_input():
    puzzle_input = open("aoc2020/day18/input.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = sum(map(calculate, content))

    assert actual == 6640667297513

    actual = sum([calculate(line, True) for line in content])

    assert actual == 451589894841552
