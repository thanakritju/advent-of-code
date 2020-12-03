from order import order


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

    actual = order(test_input)

    assert actual == "CABDFE"


def test_order_for_puzzle_input():
    puzzle_input = open("aoc2018/day7/instructions.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = order(content)

    assert actual == "OCPUEFIXHRGWDZABTQJYMNKVSL"
