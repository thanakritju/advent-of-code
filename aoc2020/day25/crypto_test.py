import pytest

from aoc2020.day25.crypto import *


def test_hack():
    actual = hack(5764801, 17807724)

    assert actual == 14897079


@pytest.mark.puzzle
def test_hack_for_puzzle():
    actual = hack(12578151, 5051300)

    assert actual == 296776
