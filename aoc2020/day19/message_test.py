import pytest

from aoc2020.day19.message import *


def test_get_valid_messages():
    puzzle_input = open("aoc2020/day19/sample.txt", "r")
    rules, messages = puzzle_input.read().split("\n\n")

    actual = get_rule(rules.splitlines(), "0")

    assert actual == "a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b"

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 2


@pytest.mark.skip(reason="will do later")
def test_get_valid_messages_2():
    puzzle_input = open("aoc2020/day19/sample2.txt", "r")
    rules, messages = puzzle_input.read().split("\n\n")

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 3

    rules = rules.replace("8: 42", "8: 42 | 42 8").replace(
        "11: 42 31", "11: 42 31 | 42 11 31")

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 12


def test_get_valid_messages_for_puzzle_input():
    puzzle_input = open("aoc2020/day19/input.txt", "r")
    rules, messages = puzzle_input.read().split("\n\n")

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 102


@pytest.mark.skip(reason="will do later")
def test_get_valid_messages_for_puzzle_input_part2():
    puzzle_input = open("aoc2020/day19/input.txt", "r")
    rules, messages = puzzle_input.read().split("\n\n")
    rules = rules.replace("8: 42", "8: 42 | 42 8").replace(
        "11: 42 31", "11: 42 31 | 42 11 31")

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 0
