import pytest

from aoc2021.day10.syntax_scoring import syntax_error_score, get_corrupted_char, incomplete_score, get_incomplete_chars


def test_syntax_error_score():
    puzzle_input = open("aoc2021/day10/sample.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = syntax_error_score(content)

    assert actual == 26397


@pytest.mark.parametrize(
    "navigation,expected,found",
    [
        ("(]", ")", "]"),
        ("()", None, None),
        ("{()()()>", "}", ">"),
        ("(((()))}", ")", "}"),
        ("<([]){()}[{}])", ">", ")"),
        ("{([(<{}[<>[]}>{[]{[(<()>", "]", "}"),
        ("[[<[([]))<([[{}[[()]]]", "]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", ")", "]"),
        ("[<(<(<(<{}))><([]([]()", ">", ")"),
        ("<{([([[(<>()){}]>(<<{{", "]", ">"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", None, None),
    ]
)
def test_get_corrupted_char(navigation, expected, found):
    actual = get_corrupted_char(navigation)

    assert actual[0] == expected
    assert actual[1] == found


@pytest.mark.puzzle
def test_syntax_error_score_for_puzzle():
    puzzle_input = open("aoc2021/day10/input.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = syntax_error_score(content)

    assert actual == 323691


@pytest.mark.parametrize(
    "navigation,expected",
    [
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[", "]"),
        ("[}", ""),
        ("()", ""),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
        ("<{([([[(<>()){}]>(<<{{", ""),
    ]
)
def test_get_incomplete_chars(navigation, expected):
    actual = get_incomplete_chars(navigation)

    assert actual == expected


def test_incomplete_score():
    puzzle_input = open("aoc2021/day10/sample.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = incomplete_score(content)

    assert actual == 288957


@pytest.mark.puzzle
def test_incomplete_score_for_puzzle():
    puzzle_input = open("aoc2021/day10/input.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = incomplete_score(content)

    assert actual == 2858785164
