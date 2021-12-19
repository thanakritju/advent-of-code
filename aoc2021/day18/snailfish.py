from itertools import permutations

OPEN_BRACKET = "["
CLOSE_BRACKET = "]"
COMMA = ","
NUMBERS = "0123456789"


class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        if self.data is None:
            return f'[{self.left},{self.right}]'
        return str(self.data)

    def print(self):
        return f"[{self.printleft()},{self.printright()}]"

    def magnitude(self):
        if self.data is not None:
            return self.data
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def printleft(self):
        return self.left.print() if self.left.data is None else self.left.data

    def printright(self):
        return self.right.print() if self.right.data is None else self.right.data


class Index:
    def __init__(self):
        self.v = 0


def largest_magnitude(content):
    mags = []
    for a, b in permutations(content.splitlines(), 2):
        node_a = read_node(a, Index())
        node_b = read_node(b, Index())
        mags.append(reduce(Node(node_a, node_b)).magnitude())
    return max(mags)


def read_node(text, index: Index):
    n = Node()
    assert text[index.v] == OPEN_BRACKET
    index.v += 1

    if text[index.v] in NUMBERS:
        n.left = Node(None, None, int(text[index.v]))
        index.v += 1
    elif text[index.v] == OPEN_BRACKET:
        n.left = read_node(text, index)

    assert text[index.v] == COMMA
    index.v += 1

    if text[index.v] in NUMBERS:
        n.right = Node(None, None, int(text[index.v]))
        index.v += 1
    elif text[index.v] == OPEN_BRACKET:
        n.right = read_node(text, index)

    assert text[index.v] == CLOSE_BRACKET
    index.v += 1

    return n


def explode(sf):
    q = [(sf, 0)]
    while q:
        node, d = q.pop()
        if d == 4 and node.data is None:
            leaves = get_leaves(sf)
            left_idx = leaves.index(node.left)
            right_idx = left_idx + 1
            if left_idx > 0:
                leaves[left_idx-1].data += node.left.data
            if right_idx + 1 < len(leaves):
                leaves[right_idx+1].data += node.right.data
            node.data, node.left, node.right = 0, None, None
            return True

        if node.data is not None:
            continue
        q.append((node.right, d+1))
        q.append((node.left, d+1))

    return False


def split(sf):
    leaves = get_leaves(sf)
    for leave in leaves:
        if leave.data > 9:
            leave.left = Node(None, None, leave.data//2)
            leave.right = Node(None, None, leave.data - leave.data//2)
            leave.data = None
            return True
    return False


def reduce(snailfish):
    while True:
        shouldContinue = explode(snailfish)
        if shouldContinue:
            continue
        shouldContinue = split(snailfish)
        if not shouldContinue:
            break
    return snailfish


def sum_snailfish(content):
    returning_node = None
    for line in content.splitlines():
        node = read_node(line, Index())
        if returning_node is None:
            returning_node = node
        else:
            returning_node = Node(returning_node, node)
        returning_node = reduce(returning_node)
    return returning_node


def get_leaves(node):
    lst = []
    q = [node]
    while q:
        node = q.pop()
        if node.data is not None:
            lst.append(node)
        else:
            q.append(node.right)
            q.append(node.left)

    return lst
