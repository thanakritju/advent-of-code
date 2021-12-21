from collections import defaultdict


def process(content, times, switch=False):
    algo, s = load_data(content)
    v = "."

    for _ in range(times):
        if switch:
            v = "#" if v == "." else "."
        s = _process(algo, s, v)

    return sum([1 for v in s.values() if v == "#"])


def _process(algo, s, defualt_value="."):
    new_s = defaultdict(lambda: defualt_value)
    q = [(0, 0)]
    while q:
        x, y = q.pop()
        new_s[(x, y)] = calculate_new_pixel(s, algo, x, y)
        if not reach_boundary(s, x, y):
            for i, j in get_neighbors(x, y):
                if (i, j) not in new_s:
                    q.append((i, j))
    return new_s


def reach_boundary(s, i, j):
    return all([s[(x, y)] == "." for x, y in get_neighbors(i, j)]) or all([s[(x, y)] == "#" for x, y in get_neighbors(i, j)])


def get_neighbors(i, j):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            yield (i+dx, j+dy)


def calculate_new_pixel(s, algo, i, j):
    binary = ""
    for x, y in get_neighbors(i, j):
        binary += "1" if s[(x, y)] == "#" else "0"
    return algo[int(binary, 2)]


def load_data(content):
    algo, grids = content.split("\n\n")
    s = defaultdict(lambda: ".")
    for j, line in enumerate(grids.splitlines()):
        for i, char in enumerate(line):
            s[(i, j)] = char

    return algo, s
