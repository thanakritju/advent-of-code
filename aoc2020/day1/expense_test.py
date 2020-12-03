import pytest

from expense import get_sum_of_two_entries, get_sum_of_three_entries


def test_get_sum_of_two_entries():
    test_input = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    actual = get_sum_of_two_entries(test_input)

    assert actual == 514579


def test_get_sum_of_three_entries():
    test_input = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    actual = get_sum_of_three_entries(test_input)

    assert actual == 241861950


@pytest.mark.puzzle
def test_get_sum_of_two_entries_for_puzzle():
    puzzle_input = open("aoc2020/day1/expense_report.txt", "r")
    content = list(map(int, puzzle_input.read().splitlines()))

    actual = get_sum_of_two_entries(content)

    assert actual == 355875


@pytest.mark.puzzle
def test_get_sum_of_three_entries_for_puzzle():
    puzzle_input = open("aoc2020/day1/expense_report.txt", "r")
    content = list(map(int, puzzle_input.read().splitlines()))

    actual = get_sum_of_three_entries(content)

    assert actual == 140379120
