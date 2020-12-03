from area import biggest_area


#    [[1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2],
#     [1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2],
#     [1, 1, 1, 4, 4, 0, 2, 2, 2, 2, 2],
#     [1, 1, 4, 4, 4, 4, 0, 0, 0, 0, 0],
#     [1, 1, 4, 4, 4, 5, 5, 5, 5, 6, 6],
#     [0, 0, 5, 5, 5, 5, 5, 5, 5, 6, 6],
#     [3, 3, 3, 3, 5, 5, 5, 5, 6, 6, 6],
#     [3, 3, 3, 3, 3, 5, 5, 6, 6, 6, 6],
#     [3, 3, 3, 3, 3, 3, 0, 6, 6, 6, 6],
#     [3, 3, 3, 3, 3, 3, 0, 6, 6, 6, 6],
#     [3, 3, 3, 3, 3, 3, 0, 6, 6, 6, 6],
#     [3, 3, 3, 3, 3, 3, 0, 6, 6, 6, 6]]
def test_biggest_area():
    test_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]

    actual = biggest_area(test_input)

    assert actual == 17


def test_biggest_area_for_puzzle_input():
    puzzle_input = open("aoc2018/day6/coordinates.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = biggest_area(content)

    assert actual == 5941
