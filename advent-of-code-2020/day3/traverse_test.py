import pytest

from traverse import traverse


test_pattern = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_traverse():
    tree_found = traverse(test_pattern)

    assert tree_found == 7


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((1, 1), 2),
        ((3, 1), 7),
        ((5, 1), 3),
        ((7, 1), 4),
        ((1, 2), 2),
    ]
)
def test_traverse_with_different_move(test_input, expected):
    tree_found = traverse(
        test_pattern, row_move=test_input[1], col_move=test_input[0])

    assert tree_found == expected


def test_traverse_for_puzzle_input():
    puzzle_input = open("advent-of-code-2020/day3/patterns.txt", "r")
    content = puzzle_input.read().splitlines()

    tree_found = traverse(content)

    assert tree_found == 176


def test_traverse_for_puzzle_input():
    puzzle_input = open("advent-of-code-2020/day3/patterns.txt", "r")
    content = puzzle_input.read().splitlines()

    tree_found = traverse(content, 1, 1)
    tree_found *= traverse(content, 1, 3)
    tree_found *= traverse(content, 1, 5)
    tree_found *= traverse(content, 1, 7)
    tree_found *= traverse(content, 2, 1)

    assert tree_found == 5872458240
