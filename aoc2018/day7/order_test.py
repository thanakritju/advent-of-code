import pytest

from order import order


@pytest.mark.timeout(1)
def test_order():
    test_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]

    actual, time = order(test_input)

    assert actual == "CABDFE"


@pytest.mark.timeout(1)
def test_order_with_workers():
    test_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]

    actual, time = order(test_input, worker_number=2, time_need=1)

    assert actual == "CABFDE"
    assert time == 15


@pytest.mark.timeout(1)
@pytest.mark.puzzle
def test_order_for_puzzle_input():
    puzzle_input = open("aoc2018/day7/instructions.txt", "r")
    content = puzzle_input.read().splitlines()

    actual, time = order(content)

    assert actual == "OCPUEFIXHRGWDZABTQJYMNKVSL"

    actual, time = order(content, worker_number=5, time_need=61)

    assert time == 991
