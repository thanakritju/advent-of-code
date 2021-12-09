def count_low_points(lines):
    locations = load_data(lines)
    len_y = len(locations)
    len_x = len(locations[0])

    count = 0
    for j in range(len_y):
        for i in range(len_x):
            if is_lowest_point(i, j, locations):
                count += locations[j][i] + 1

    return count


def largest_three_basin(lines):
    locations = load_data(lines)
    len_y = len(locations)
    len_x = len(locations[0])

    areas = []
    for j in range(len_y):
        for i in range(len_x):
            if is_lowest_point(i, j, locations):
                areas.append(get_basin_area(i, j, locations))

    areas = sorted(areas)
    return areas[-1] * areas[-2] * areas[-3]


def get_basin_area(i, j, locations):
    visited = {}
    queue = [(i, j)]
    while queue:
        x, y = queue.pop()
        if (x, y) not in visited:
            visited[(x, y)] = True
            for each_x, each_y in get_neighbors(x, y, locations):
                if locations[y][x] < locations[each_y][each_x] and locations[each_y][each_x] != 9:
                    queue.append((each_x, each_y))

    return len(visited)


def is_lowest_point(i, j, locations):
    return all([locations[j][i] < locations[y][x] for x, y in get_neighbors(i, j, locations)])


def get_neighbors(i, j, locations):
    len_y = len(locations)
    len_x = len(locations[0])
    for each in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x = i + each[0]
        y = j + each[1]

        if (x < 0 or y < 0 or x >= len_x or y >= len_y):
            continue
        else:
            yield (x, y)


def load_data(lines):
    return [list(map(int, line)) for line in lines]
