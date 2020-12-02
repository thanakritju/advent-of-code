import pytest

from password import password_check, password_check_v2, count_valid_password, count_valid_password_v2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1-3 a: abcde", True),
        ("1-3 b: cdefg", False),
        ("2-9 c: ccccccccc", True),
    ]
)
def test_password_check(test_input, expected):
    actual = password_check(test_input)

    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1-3 a: abcde", True),
        ("1-3 b: cdefg", False),
        ("2-9 c: ccccccccc", False),
    ]
)
def test_password_check_v2(test_input, expected):
    actual = password_check_v2(test_input)

    assert actual == expected


@pytest.mark.puzzle
def test_get_sum_of_three_entries_for_puzzle():
    puzzle_input = open("advent-of-code-2020/day2/passwords.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_valid_password(content)

    assert actual == 393


@pytest.mark.puzzle
def test_get_sum_of_three_entries_for_puzzle():
    puzzle_input = open("advent-of-code-2020/day2/passwords.txt", "r")
    content = puzzle_input.read().splitlines()

    actual = count_valid_password_v2(content)

    assert actual == 690
