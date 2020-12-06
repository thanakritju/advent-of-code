from answer import count_answer, count_answered_by_everyone


def test_count_answer():
    test_input = [
        ["abc"],
        ["a", "b", "c"],
        ["ab", "ac"],
        ["a", "a", "a", "a"],
        ["b"]
    ]

    actual = count_answer(test_input)

    assert actual == 11


def test_count_answer():
    test_input = [
        ["abc"],
        ["a", "b", "c"],
        ["ab", "ac"],
        ["a", "a", "a", "a"],
        ["b"]
    ]

    actual = count_answered_by_everyone(test_input)

    assert actual == 6


def test_count_answer_for_puzzle_input():
    puzzle_input = open("aoc2020/day6/answers.txt", "r")
    content = puzzle_input.read().split('\n\n')
    content = list(map(lambda x: x.splitlines(), content))

    actual = count_answer(content)

    assert actual == 6542


def test_count_answered_by_everyone_for_puzzle_input():
    puzzle_input = open("aoc2020/day6/answers.txt", "r")
    content = puzzle_input.read().split('\n\n')
    content = list(map(lambda x: x.splitlines(), content))

    actual = count_answered_by_everyone(content)

    assert actual == 3299
