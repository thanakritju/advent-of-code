from checksum import checksum, get_common_id


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


def test_checksum_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day2/box_ids.txt", "r")
    content = puzzle_input.read().split()

    actual = checksum(content)

    assert actual == 8118
