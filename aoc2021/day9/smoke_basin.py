def count_low_points(lines):
    locations = load_data(lines)
    len_y = len(locations)
    len_x = len(locations[0])

    count = 0
    for j in range(len_y):
        for i in range(len_x):
            if all([locations[j][i] < locations[y][x] for x, y in get_neighbors(i, j, locations)]):
                count += locations[j][i] + 1

    return count


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
