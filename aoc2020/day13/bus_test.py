import pytest

from aoc2020.day13.bus import *


def test_get_earliest_bus():
    test_input = [
        "939",
        "7,13,x,x,59,x,31,19",
    ]

    actual = get_earliest_bus(test_input)

    assert actual == 295


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("7,13,x,x,59,x,31,19", 1068781),
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ]
)
def test_get_earliest_bus(test_input, expected):
    actual = get_earliest_time(test_input)

    assert actual == expected


@pytest.mark.timeout(2)
def test_get_earliest_bus_for_puzzle_input():
    puzzle_input = open("aoc2020/day13/bus_time.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = get_earliest_bus(content)

    assert actual == 5946

    actual = get_earliest_time(content[1])

    assert actual == 645338524823718
