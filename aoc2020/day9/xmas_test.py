from aoc2020.day9.xmas import find_weakness, exploit_weakness


def test_find_weakness():
    test_input = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]

    actual = find_weakness(test_input, preamble=5)

    assert actual == 127

    actual = exploit_weakness(test_input, weakness=127)

    assert actual == 62


def test_run_for_puzzle_input():
    puzzle_input = open("aoc2020/day9/numbers.txt", "r")
    content = puzzle_input.read().splitlines()
    content = list(map(int, content))

    actual = find_weakness(content, preamble=25)

    assert actual == 104054607

    actual = exploit_weakness(content, weakness=104054607)

    assert actual == 13935797
