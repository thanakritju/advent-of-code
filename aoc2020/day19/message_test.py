from aoc2020.day19.message import *


def test_get_valid_messages():
    puzzle_input = open("aoc2020/day19/sample.txt", "r")
    rules, messages = puzzle_input.read().split("\n\n")

    actual = get_rule(rules.splitlines(), "0")

    assert actual == "a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b"

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 2


def test_get_valid_messages_for_puzzle_input():
    puzzle_input = open("aoc2020/day19/input.txt", "r")
    rules, messages = puzzle_input.read().split("\n\n")

    actual = get_valid_messages(rules.splitlines(), messages.splitlines())

    assert actual == 2
