from fabric import get_overlap


def test_get_overlap():
    test_input = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]

    actual = get_overlap(test_input)

    assert actual == 4


def test_get_overlap_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day3/fabrics.txt", "r")
    content = puzzle_input.read().split()

    actual = get_overlap(content)

    assert actual == True
