import pytest

from aoc2021.day21.game import play, play_quantum


def test_play():
    actual = play(4, 8)

    assert actual == 739785


@pytest.mark.puzzle
def test_play_for_puzzle():
    actual = play(9, 6)

    assert actual == 1004670


def test_play_quantum():
    actual = play_quantum(4, 0, 8, 0)

    assert max(actual) == 444356092776315


@pytest.mark.puzzle
def test_play_quantum_for_puzzle():
    actual = play_quantum(9, 0, 6, 0)

    assert max(actual) == 492043106122795
