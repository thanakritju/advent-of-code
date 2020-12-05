import pytest

from seat import get_seat_id, get_seat_location, get_missing_id


@pytest.mark.parametrize(
    "test_seat,expected_seat_id,expected_seat_location",
    [
        ("FBFBBFFRLR", 357, (44, 5)),
        ("BFFFBBFRRR", 567, (70, 7)),
        ("FFFBBBFRRR", 119, (14, 7)),
        ("BBFFBBFRLL", 820, (102, 4)),
    ]
)
def test_seat(test_seat, expected_seat_id, expected_seat_location):
    seat_location = get_seat_location(test_seat)
    seat_id = get_seat_id(test_seat)

    assert seat_location == expected_seat_location
    assert seat_id == expected_seat_id


def test_seat_for_puzzle_input():
    puzzle_input = open("aoc2020/day5/seats.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = max(list(map(get_seat_id, content)))

    assert actual == 926


def test_seat_finding_the_seat_for_puzzle_input():
    puzzle_input = open("aoc2020/day5/seats.txt", "r")
    content = puzzle_input.read().splitlines()

    my_seat_id = get_missing_id(content)

    assert my_seat_id == 657
