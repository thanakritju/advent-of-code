import copy


def get_all_actives_4d(content, cycles=6):
    space = parse_input(content)
    big_space = create_big_space(space, cycles)
    count = 0
    while count < cycles:
        big_space = run(big_space)
        count += 1

    return count_all(big_space)


def count_all(space, cell_type="#"):
    count = 0
    for z in space:
        for y in z:
            for x in y:
                count += x.count("#")
    return count


def run(space):
    successor = copy.deepcopy(space)
    for k, z in enumerate(space):
        for j, y in enumerate(z):
            for i, x in enumerate(y):
                for h, w in enumerate(x):
                    successor[k][j][i][h] = transform(
                        w, list(get_adj(space, h, i, j, k)))

    return successor


def transform(itself, neighbors):
    actives = neighbors.count("#")
    if itself == "#":
        if actives == 2 or actives == 3:
            return "#"
        else:
            return "."
    else:
        if actives == 3:
            return "#"
        else:
            return "."


def get_adj(space, w, x, y, z):
    adjacency = [
        (h, i, j, k)
        for h in (-1, 0, 1)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        for k in (-1, 0, 1)
        if not (i == j == k == h == 0)
    ]
    for dw, dx, dy, dz in adjacency:
        try:
            yield space[z + dz][y + dy][x + dx][w + dw]
        except:
            pass


def parse_input(content):
    return [list(line) for line in content.splitlines()]


def create_big_space(space, cycles):
    max_n = len(space) + cycles * 2
    big_space = [
        [
            [
                ['.' for w in range(max_n)]
                for x in range(max_n)
            ]
            for y in range(1 + cycles * 2)
        ]
        for z in range(1 + cycles * 2)
    ]
    for j, y in enumerate(space):
        for i, x in enumerate(y):
            big_space[cycles][cycles][j + cycles][i + cycles] = x

    return big_space
