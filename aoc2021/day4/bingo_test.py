import pytest

from aoc2021.day4.bingo import get_final_score, get_final_score_for_last_board


def test_get_final_score():
    puzzle_input = open("aoc2021/day4/sample.txt", "r")
    content = list(map(str, puzzle_input.read().split("\n\n")))

    actual = get_final_score(content)

    assert actual == 4512


@pytest.mark.puzzle
def test_get_final_score_for_puzzle():
    puzzle_input = open("aoc2021/day4/input.txt", "r")
    content = list(map(str, puzzle_input.read().split("\n\n")))

    actual = get_final_score(content)

    assert actual == 8580


def test_get_final_score_for_last_board():
    puzzle_input = open("aoc2021/day4/sample.txt", "r")
    content = list(map(str, puzzle_input.read().split("\n\n")))

    actual = get_final_score_for_last_board(content)

    assert actual == 1924


@pytest.mark.puzzle
def test_get_final_score_for_last_board_for_puzzle():
    puzzle_input = open("aoc2021/day4/input.txt", "r")
    content = list(map(str, puzzle_input.read().split("\n\n")))

    actual = get_final_score_for_last_board(content)

    assert actual == 9576
