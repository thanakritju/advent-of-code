from collections import deque


def count_flashes(content, steps):
    octopuses = load_data(content)
    flashes = 0
    for _ in range(steps):
        octopuses, flashes = process(octopuses, flashes)

    return flashes


def when_to_flash(content):
    octopuses = load_data(content)
    i = 1
    flashes = 0
    previous_flashes = 0
    while True:
        octopuses, flashes = process(octopuses, flashes)
        if flashes - previous_flashes == 100:
            return i
        previous_flashes = flashes
        i += 1


def process(octopuses, flashes):
    queue = deque()
    new_octopuses = []
    for j, line in enumerate(octopuses):
        t = []
        for i, octopus in enumerate(line):
            if octopus == 9:
                queue.append((i, j))
            t.append(octopus + 1)
        new_octopuses.append(t)

    flashed = set()
    while queue:
        i, j = queue.pop()
        if (i, j) not in flashed:
            flashed.add((i, j))
            flashes += 1
            for x, y in get_adjacents(new_octopuses, i, j):
                new_octopuses[y][x] = new_octopuses[y][x] + 1
                if new_octopuses[y][x] > 9 and (x, y) not in flashed:
                    queue.append((x, y))

    new_octopuses = [
        [0 if octopus > 9 else octopus for octopus in line]
        for line in new_octopuses
    ]

    return new_octopuses, flashes


def get_adjacents(octopuses, i, j):
    directions = [
        (dx+i, dy+j)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if not (dx == 0 and dy == 0)
    ]
    for x, y in directions:
        if x >= 0 and y >= 0 and x < len(octopuses[0]) and y < len(octopuses):
            yield (x, y)


def load_data(lines):
    return [
        [int(octopus) for octopus in line]
        for line in lines
    ]
