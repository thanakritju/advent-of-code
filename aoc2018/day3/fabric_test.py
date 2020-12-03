import pytest

from fabric import get_overlap, extract_input, get_the_isolate_id


def test_get_overlap():
    test_input = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]

    actual = get_overlap(test_input)

    assert actual == 4


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("#1 @ 1,3: 2x2", set([(1, 3), (1, 4), (2, 3), (2, 4)])),
        ("#2 @ 3,1: 2x2", set([(3, 1), (4, 1), (3, 2), (4, 2)])),
        ("#3 @ 1,1: 1x2", set([(1, 1), (1, 2)])),
        ("#4 @ 1,0: 2x1", set([(1, 0), (2, 0)])),
    ]
)
def test_extract_input(test_input, expected):
    actual = extract_input(test_input)

    assert actual == expected


def test_get_the_isolate_id():
    test_input = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]

    actual = get_the_isolate_id(test_input)

    assert actual == 3


@pytest.mark.puzzle
def test_get_overlap_for_puzzle_input():
    puzzle_input = open("aoc2018/day3/fabrics.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = get_overlap(content)

    assert actual == 106501


@pytest.mark.puzzle
def test_get_the_isolate_id_for_puzzle_input():
    puzzle_input = open("aoc2018/day3/fabrics.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = get_the_isolate_id(content)

    assert actual == 632
