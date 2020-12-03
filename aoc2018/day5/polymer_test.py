import pytest

from polymer import react_polymer, is_reacted, optimized_react_polymer


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("dabAcCaCBAcCcaDA", "dabCBAcaDA"),
        ("aA", ""),
        ("abBA", ""),
        ("aabAAB", "aabAAB"),
    ]
)
def test_react_polymer(test_input, expected):
    actual = react_polymer(test_input)

    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("A", "A"), False),
        (("a", "A"), True),
        (("A", "c"), False),
        (("B", "b"), True),
    ]
)
def test_is_reacted(test_input, expected):
    actual = is_reacted(test_input[0], test_input[1])

    assert actual == expected


@pytest.mark.puzzle
def test_react_polymer_for_puzzle_input():
    puzzle_input = open("aoc2018/day5/polymers.txt", "r")
    content = puzzle_input.read()

    actual = react_polymer(content)

    assert len(actual) == 11194


@pytest.mark.puzzle
def test_react_polymer_for_puzzle_input():
    puzzle_input = open("aoc2018/day5/polymers.txt", "r")
    content = puzzle_input.read()

    actual = optimized_react_polymer(content)

    assert actual == 4178
