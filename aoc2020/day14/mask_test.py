from aoc2020.day14.mask import *


def test_get_mask_results():
    test_input = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]

    results = get_mask_results(test_input)

    assert sum(results.values()) == 165


def test_get_mask_results():
    test_input = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]

    results = get_mask_results_v2(test_input)

    assert sum(results.values()) == 208


def test_get_mask_results_for_puzzle_input():
    puzzle_input = open("aoc2020/day14/input.txt", "r")
    content = puzzle_input.read().splitlines()

    results = get_mask_results(content)

    assert sum(results.values()) == 9879607673316

    results = get_mask_results_v2(content)

    assert sum(results.values()) == 3435342392262
