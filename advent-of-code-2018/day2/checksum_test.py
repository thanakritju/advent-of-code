import pytest

from checksum import checksum, get_common_id, is_close, drop_duplicate


def test_checksum():
    test_input = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]
    actual = checksum(test_input)

    assert actual == 12


def test_get_common_id():
    test_input = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    actual = get_common_id(test_input)

    assert actual == "fgij"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("abcde", "fghij"), False),
        (("abcde", "wvxyz"), False),
        (("fguij", "fghij"), True),
    ]
)
def test_is_close(test_input, expected):
    actual = is_close(test_input[0], test_input[1])

    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("abcde", "fghij"), ""),
        (("abcde", "axcye"), "ace"),
        (("fguij", "fghij"), "fgij"),
    ]
)
def test_is_close(test_input, expected):
    actual = drop_duplicate(test_input[0], test_input[1])

    assert actual == expected


@pytest.mark.puzzle
def test_checksum_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day2/box_ids.txt", "r")
    content = puzzle_input.read().split()

    actual = checksum(content)

    assert actual == 8118


@pytest.mark.puzzle
def test_checksum_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day2/box_ids.txt", "r")
    content = puzzle_input.read().split()

    actual = get_common_id(content)

    assert actual == 'jbbenqtlaxhivmwyscjukztdp'
