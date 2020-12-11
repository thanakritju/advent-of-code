import pytest

from aoc2020.day11.seat_model import count_seat, get_new_seat, get_new_seat_v2


test_input = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]


@pytest.mark.timeout(0.1)
def test_count_seat():

    actual = count_seat(test_input, get_new_seat)

    assert actual == 37


@pytest.mark.timeout(0.1)
def test_count_seat_v2():
    actual = count_seat(test_input, get_new_seat_v2)

    assert actual == 26


@pytest.mark.puzzle
def test_count_seat_for_puzzle_input():
    puzzle_input = open("aoc2020/day11/seats.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_seat(content, get_new_seat)

    assert actual == 2321

    actual = count_seat(content, get_new_seat_v2)

    assert actual == 2102
