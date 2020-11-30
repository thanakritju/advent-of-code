import pytest

from main import calculate_frequency


@pytest.mark.parametrize("test_input,expected", 
    [
        (["+1", "+1", "+1"], 3), 
        (["+1", "+1", "-2"], 0), 
        (["-1", "-2", "-3"], -6),
    ]
)
def test_calculate_frequency(test_input, expected):
    actual = calculate_frequency(test_input)

    assert actual == expected



def test_calculate_frequency_for_long_input():
    puzzle_input = open("advent-of-code-2018/day1/frequency.txt", "r")
    content = puzzle_input.read().split()

    actual = calculate_frequency(content)

    assert actual == 538