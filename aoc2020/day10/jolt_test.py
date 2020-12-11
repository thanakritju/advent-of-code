from aoc2020.day10.jolt import get_jolt_differences, count_jolt_arrangements


def test_get_jolt_differences():
    test_input = [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4,
    ]

    jolt_1, jolt_3 = get_jolt_differences(test_input)

    assert jolt_1 == 7
    assert jolt_3 == 5

    arrangements = count_jolt_arrangements(test_input)

    assert arrangements == 8


def test_get_jolt_differences_2():
    test_input = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]

    jolt_1, jolt_3 = get_jolt_differences(test_input)

    assert jolt_1 == 22
    assert jolt_3 == 10

    arrangements = count_jolt_arrangements(test_input)

    assert arrangements == 19208


def test_get_jolt_differences_for_puzzle_input():
    puzzle_input = open("aoc2020/day10/jolts.txt", "r")
    content = puzzle_input.read().splitlines()
    content = list(map(int, content))

    jolt_1, jolt_3 = get_jolt_differences(content)
    multiple = jolt_1 * jolt_3

    assert multiple == 2059
