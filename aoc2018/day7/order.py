import re
from typing import Sequence, Tuple


def order(instructions: Sequence[str]) -> str:
    return list(map(parse_input, instructions))


def parse_input(instruction: str) -> Tuple[str, str]:
    m = re.search(
        r"Step (?P<source>.) must be finished before step (?P<dest>.) can begin.", instruction)
    return m.group('source'), m.group('dest')
