import pytest

from frequency import calculate_frequency, calculate_first_reaches_twice


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["+1", "+1", "+1"], 3),
        (["+1", "+1", "-2"], 0),
        (["-1", "-2", "-3"], -6),
    ]
)
def test_calculate_frequency(test_input, expected):
    actual = calculate_frequency(test_input)

    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["+1", "-2", "+3", "+1"], 2),
        (["+1", "-1"], 0),
        (["+3", "+3", "+4", "-2", "-4"], 10),
        (["-6", "+3", "+8", "+5", "-6"], 5),
        (["+7", "+7", "-2", "-7", "-4"], 14),
    ]
)
def test_calculate_first_reaches_twice(test_input, expected):
    actual = calculate_first_reaches_twice(test_input)

    assert actual == expected


@pytest.mark.puzzle
def test_calculate_frequency_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day1/frequency.txt", "r")
    content = puzzle_input.read().split()

    actual = calculate_frequency(content)

    assert actual == 538


@pytest.mark.puzzle
def test_calculate_frequency_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day1/frequency.txt", "r")
    content = puzzle_input.read().split()

    actual = calculate_first_reaches_twice(content)

    assert actual == 77271
