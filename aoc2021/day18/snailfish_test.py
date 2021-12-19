import pytest

from aoc2021.day18.snailfish import explode, read_node, sum_snailfish, Index, get_leaves, largest_magnitude


@pytest.mark.parametrize(
    "snailfish,expected",
    [
        ("[1,4]", (1, 4)),
        ("[1,[1,2]]", (1, "[1,2]")),
        ("[[1,2],1]", ("[1,2]", 1)),
        ("[[[[[9,8],1],2],3],4]", ("[[[[9,8],1],2],3]", 4)),
    ]
)
def test_read_node(snailfish, expected):
    actual = read_node(snailfish, Index())

    assert (actual.printleft(), actual.printright()) == expected


@pytest.mark.parametrize(
    "snailfish,expected",
    [
        ("[1,4]", [1, 4]),
        ("[1,[1,2]]", [1, 1, 2]),
        ("[[1,2],1]", [1, 2, 1]),
        ("[[[[[9,8],1],2],3],4]", [9, 8, 1, 2, 3, 4]),
        ("[[6,[5,[4,[3,2]]]],1]", [6, 5, 4, 3, 2, 1]),
    ]
)
def test_get_leaves(snailfish, expected):
    node = read_node(snailfish, Index())

    actual = get_leaves(node)

    assert list(map(lambda x: x.data, actual)) == expected


@pytest.mark.parametrize(
    "snailfish,expected",
    [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
         "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
    ]
)
def test_explode(snailfish, expected):
    snailfish = read_node(snailfish, Index())

    explode(snailfish)

    assert snailfish.print() == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("sample1.txt", "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
        ("sample2.txt", "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
        ("sample3.txt", "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
        ("sample4.txt",
         "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"),
        ("sample.txt",
         "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"),
    ]
)
def test_sum_snailfish(filename, expected):
    puzzle_input = open(f"aoc2021/day18/{filename}", "r")
    content = puzzle_input.read()

    actual = sum_snailfish(content)

    assert actual.print() == expected


@pytest.mark.parametrize(
    "snailfish,expected",
    [
        ("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", 4140),
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
        ("[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]", 3993),
    ]
)
def test_magnitude(snailfish, expected):
    snailfish = read_node(snailfish, Index())

    actual = snailfish.magnitude()

    assert actual == expected


@pytest.mark.puzzle
def test_magnitude_for_puzzle():
    puzzle_input = open(f"aoc2021/day18/input.txt", "r")
    content = puzzle_input.read()

    actual = sum_snailfish(content)

    assert actual.magnitude() == 4176


def test_largest_magnitude():
    puzzle_input = open(f"aoc2021/day18/sample4.txt", "r")
    content = puzzle_input.read()

    actual = largest_magnitude(content)

    assert actual == 3993


@pytest.mark.puzzle
def test_largest_magnitude_for_puzzle():
    puzzle_input = open(f"aoc2021/day18/input.txt", "r")
    content = puzzle_input.read()

    actual = largest_magnitude(content)

    assert actual == 0
