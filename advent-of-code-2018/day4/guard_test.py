from datetime import datetime

import pytest

from guard import guard, parse_action


def test_guard():
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

    actual = guard(test_input)

    assert actual == 240


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
