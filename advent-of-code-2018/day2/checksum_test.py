from checksum import checksum

test_input = [
    "abcdef", 
    "bababc",
    "abbcde", 
    "abcccd",
    "aabcdd", 
    "abcdee",
    "ababab",
]

def test_checksum():
    actual = checksum(test_input)

    assert actual == 12

def test_checksum_for_puzzle_input():
    puzzle_input = open("advent-of-code-2018/day2/box_ids.txt", "r")
    content = puzzle_input.read().split()

    actual = checksum(content)

    assert actual == 8118