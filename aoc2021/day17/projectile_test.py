import pytest

from aoc2021.day17.projectile import highest_y, get_highest_y, get_all_initial_velocities


def test_highest_y():
    actual = highest_y("target area: x=20..30, y=-10..-5")

    assert actual == 45


def test_get_all_initial_velocities():
    actual = get_all_initial_velocities("target area: x=20..30, y=-10..-5")

    assert actual == 112


@pytest.mark.parametrize(
    "params,expected",
    [
        ((7, 2, 20, 30, -10, -5), (3, True)),
        ((6, 3, 20, 30, -10, -5), (6, True)),
        ((9, 0, 20, 30, -10, -5), (0, True)),
        ((30, -10, 20, 30, -10, -5), (0, True)),
        ((17, -4, 20, 30, -10, -5), (0,  False)),
        ((6, 9, 20, 30, -10, -5), (45,  True)),
    ]
)
def test_get_highest_y(params, expected):
    vx, vy, min_x, max_x, min_y, max_y = params
    actual = get_highest_y(vx, vy, min_x, max_x, min_y, max_y)

    assert actual == expected


@pytest.mark.puzzle
def test_highest_y_for_puzzle():
    actual = highest_y("target area: x=94..151, y=-156..-103")

    assert actual == 12090


@pytest.mark.puzzle
def test_get_all_initial_velocities_for_puzzle():
    actual = get_all_initial_velocities("target area: x=94..151, y=-156..-103")

    assert actual == 5059
