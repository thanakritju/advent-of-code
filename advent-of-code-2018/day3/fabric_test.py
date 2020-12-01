import pytest

from fabric import get_overlap, is_overlap, extract_input


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
        (("#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4"), True),
        (("#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"), False),
        (("#1 @ 1,3: 4x4", "#3 @ 5,5: 2x2"), False),
    ]
)
def test_is_overlap(test_input, expected):
    actual = is_overlap(test_input[0], test_input[1])

    assert actual == expected


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


@pytest.mark.puzzle
def test_get_overlap_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day3/fabrics.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = get_overlap(content)

    assert actual == 106501
