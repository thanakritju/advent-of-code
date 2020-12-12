from aoc2020.day12.ship import get_distance, get_distance_with_waypoint


test_input = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


def test_get_distance():
    distance = get_distance(test_input)

    assert distance == 25


def test_get_distance_with_waypoint():
    distance = get_distance_with_waypoint(test_input)

    assert distance == 286


def test_get_distance_for_puzzle_input():
    puzzle_input = open("aoc2020/day12/ship_movements.txt", "r")
    content = puzzle_input.read().splitlines()

    distance = get_distance(content)

    assert distance == 1133

    distance = get_distance_with_waypoint(content)

    assert distance == 25
