import pytest

from handheld import run, find_correct_program


def test_run():
    test_input = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]

    actual = run(test_input)

    assert actual == 5

    actual = find_correct_program(test_input)

    assert actual == 8


@pytest.mark.puzzle
def test_run_for_puzzle_input():
    puzzle_input = open("aoc2020/day8/instructions.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = run(content)

    assert actual == 1801

    actual = find_correct_program(content)

    assert actual == 2060
