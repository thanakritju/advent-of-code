import pytest

from aoc2021.day7.crab import cal_fuel, cheapest_fuel, cal_fuel_v2, cheapest_fuel_v2


sample_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.mark.parametrize(
    "crabs,position,expected",
    [
        (sample_crabs, 2, 37),
        (sample_crabs, 1, 41),
        (sample_crabs, 3, 39),
        (sample_crabs, 10, 71),
    ]
)
def test_cal_fuel(crabs, position, expected):
    actual = cal_fuel(crabs, position)

    assert actual == expected


def test_cheapest_fuel():
    actual = cheapest_fuel(sample_crabs)

    assert actual == 37


@pytest.mark.puzzle
def test_cheapest_fuel_for_puzzle():
    puzzle_input = open("aoc2021/day7/input.txt", "r")
    content = list(map(int, puzzle_input.read().split(",")))

    actual = cheapest_fuel(content)

    assert actual == 328187


@pytest.mark.parametrize(
    "crabs,position,expected",
    [
        (sample_crabs, 5, 168),
        (sample_crabs, 2, 206),
    ]
)
def test_cal_fuel_v2(crabs, position, expected):
    actual = cal_fuel_v2(crabs, position)

    assert actual == expected


@pytest.mark.puzzle
def test_cheapest_fuel_v2_for_puzzle():
    puzzle_input = open("aoc2021/day7/input.txt", "r")
    content = list(map(int, puzzle_input.read().split(",")))

    actual = cal_fuel_v2(content, 464)

    assert actual == 91257582

    actual = cal_fuel_v2(content, 465)

    assert actual == 91257681
