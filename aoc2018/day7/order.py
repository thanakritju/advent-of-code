import re
from typing import Sequence, Tuple


def order(instructions: Sequence[str]) -> str:
    edges = set(map(parse_input, instructions))
    sources = set(map(lambda x: x[0], edges))
    dests = set(map(lambda x: x[1], edges))

    queue = sorted(list(sources.difference(dests)))
    out = []
    while (len(queue) != 0):
        node = queue.pop(0)
        prerequisites = [edge[0] for edge in edges if node == edge[1]]
        if(all(each in out for each in prerequisites)):
            out.append(node)
            queue += [edge[1] for edge in edges if node ==
                      edge[0] and edge[1] not in queue]
            queue = sorted(queue)
        else:
            queue.append(node)

    return "".join(out)


def parse_input(instruction: str) -> Tuple[str, str]:
    m = re.search(
        r"Step (?P<source>.) must be finished before step (?P<dest>.) can begin.", instruction)
    return m.group('source'), m.group('dest')
