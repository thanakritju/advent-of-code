import pytest

from aoc2020.day7.bag import count_bag, extract_bag, get_all_bags


def test_count_shiny_gold_bag():
    test_input = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]

    actual = count_bag(test_input, "shiny gold")

    assert actual == 4

    actual = get_all_bags(test_input, "shiny gold")

    assert actual == 32


def test_get_all_bags():
    test_input = [
        "shiny gold bags contain 2 dark red bags.",
        "dark red bags contain 2 dark orange bags.",
        "dark orange bags contain 2 dark yellow bags.",
        "dark yellow bags contain 2 dark green bags.",
        "dark green bags contain 2 dark blue bags.",
        "dark blue bags contain 2 dark violet bags.",
        "dark violet bags contain no other bags.",
    ]

    actual = get_all_bags(test_input, "shiny gold")

    assert actual == 126


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("faded blue bags", ("faded blue", None)),
        ("5 faded blue bags", ("faded blue", 5)),
        ("1 shiny gold bag", ("shiny gold", 1)),
        (" 4 dotted black bag", ("dotted black", 4)),
    ]
)
def test_extract_bag(test_input, expected):
    actual = extract_bag(test_input)

    assert actual == expected


def test_count_shiny_gold_bag_for_puzzle_input():
    puzzle_input = open("aoc2020/day7/bags.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_bag(content, "shiny gold")

    assert actual == 139


def test_count_shiny_gold_bag_for_puzzle_input():
    puzzle_input = open("aoc2020/day7/bags.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = get_all_bags(content, "shiny gold")

    assert actual == 58175
