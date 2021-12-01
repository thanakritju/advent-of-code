import pytest

from aoc2021.day1.main import get_number_of_increase_measurement, get_number_of_increase_measurement_in_three_sliding_window


def test_get_number_of_increase_measurement():
    test_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]

    actual = get_number_of_increase_measurement(test_input)

    assert actual == 7


def test_get_number_of_increase_measurement_in_three_sliding_window():
    test_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]

    actual = get_number_of_increase_measurement_in_three_sliding_window(
        test_input)

    assert actual == 5


@pytest.mark.puzzle
def testget_number_of_increase_measurement_for_puzzle():
    puzzle_input = open("aoc2021/day1/report.txt", "r")
    content = list(map(int, puzzle_input.read().splitlines()))

    actual = get_number_of_increase_measurement(content)

    assert actual == 1527


@pytest.mark.puzzle
def test_get_number_of_increase_measurement_in_three_sliding_window_for_puzzle():
    puzzle_input = open("aoc2021/day1/report.txt", "r")
    content = list(map(int, puzzle_input.read().splitlines()))

    actual = get_number_of_increase_measurement_in_three_sliding_window(
        content)

    assert actual == 1575
