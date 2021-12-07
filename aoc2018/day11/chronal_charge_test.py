import pytest

from aoc2018.day11.chronal_charge import get_power_level, get_coordinate, get_coordinate_and_size


@pytest.mark.parametrize(
    "x,y,serial_number,expected",
    [
        (3, 5, 8, 4),
        (122, 79, 57, -5),
        (217, 196, 39, 0),
        (101, 153, 71, 4),
    ]
)
def test_get_power_level(x, y, serial_number, expected):
    actual = get_power_level(x, y, serial_number)

    assert actual == expected


# @pytest.mark.puzzle
def test_get_coordinate_for_puzzle():
    max_x, max_y, size = get_coordinate(7857, 3)

    assert (max_x, max_y) == (243, 16)


# @pytest.mark.puzzle
def test_get_coordinate_for_puzzle():
    max_x, max_y, size = get_coordinate_and_size(7857)

    assert (max_x, max_y, size) == (243, 16, 0)
