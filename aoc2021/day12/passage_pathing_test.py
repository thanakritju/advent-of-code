import pytest

from aoc2021.day12.passage_pathing import count_paths, count_paths_v2


@pytest.mark.parametrize(
    "file_name,expected",
    [
        ("aoc2021/day12/sample.txt", 10),
        ("aoc2021/day12/sample2.txt", 19),
        ("aoc2021/day12/sample3.txt", 226),
    ]
)
def test_count_paths(file_name, expected):
    puzzle_input = open(file_name, "r")
    content = puzzle_input.read().splitlines()

    actual = count_paths(content)

    assert actual == expected


@pytest.mark.parametrize(
    "file_name,expected",
    [
        ("aoc2021/day12/sample.txt", 36),
        ("aoc2021/day12/sample2.txt", 103),
        ("aoc2021/day12/sample3.txt", 3509),
    ]
)
def test_count_paths(file_name, expected):
    puzzle_input = open(file_name, "r")
    content = puzzle_input.read().splitlines()

    actual = count_paths_v2(content)

    assert actual == expected


def test_count_paths_for_puzzle():
    puzzle_input = open("aoc2021/day12/input.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_paths(content)

    assert actual == 4707


# def test_count_paths_v2_for_puzzle():
#     puzzle_input = open("aoc2021/day12/input.txt", "r")
#     content = puzzle_input.read().splitlines()

#     actual = count_paths_v2(content)

#     assert actual == 0
