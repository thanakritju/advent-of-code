from datetime import datetime

import pytest

from guard import guard, parse_action, State, reduce_guard, Guard, update_guard, find_most_frequency


test_input = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up",
]


def test_guard():
    actual = guard(test_input)

    assert actual == 240


def test_find_most_frequency():
    actual = find_most_frequency(test_input)

    assert actual == 4455


def test_reduce_guard():
    state = State()

    state = reduce_guard(state, "[1518-11-01 00:00] Guard #10 begins shift")
    state = reduce_guard(state, "[1518-11-01 00:05] falls asleep")
    state = reduce_guard(state, "[1518-11-01 00:25] wakes up")

    assert state.active_guard.sleep_time_in_minute == 20


def test_update_guard():
    guard = Guard(0)
    guard.last_start_sleep_time_stamp = datetime(1518, 11, 1, 0, 5)

    update_guard(guard, datetime(1518, 11, 1, 0, 10))

    assert guard.sleep_time_in_minute == 5
    assert guard.frequency[5] == 1
    assert guard.frequency[10] == 0


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("[1518-11-01 00:00] Guard #10 begins shift",
         (datetime(1518, 11, 1, 0, 0), "shift_change", 10)),
        ("[1518-11-01 00:05] falls asleep",
         (datetime(1518, 11, 1, 0, 5), "sleep", None)),
        ("[1518-11-01 00:25] wakes up",
         (datetime(1518, 11, 1, 0, 25), "wake", None)),
        ("[1518-11-01 00:55] Guard #99 begins shift",
         (datetime(1518, 11, 1, 0, 55), "shift_change", 99)),
    ]
)
def test_parse_action(test_input, expected):
    actual = parse_action(test_input)

    assert actual == expected


@pytest.mark.puzzle
def test_guard_for_puzzle_input():
    puzzle_input = open("aoc2018/day4/guard_logs.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = guard(content)

    assert actual == 102688


@pytest.mark.puzzle
def test_find_most_frequency_for_puzzle_input():
    puzzle_input = open("aoc2018/day4/guard_logs.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = find_most_frequency(content)

    assert actual == 56901
