def get_power_level(x, y, serial_number):
    rack_id = x + 10
    return int(str((rack_id * y + serial_number) * rack_id // 100)[-1]) - 5


def get_coordinate(serial_number, square_size):
    cache = {}
    cell_size = 300
    cells = [
        [get_power_level(i, j, serial_number) for i in range(cell_size)]
        for j in range(cell_size)
    ]

    return find_max_value(cells, cell_size, square_size, cache)


def find_max_value(cells, cell_size, square_size, cache):
    max_value = 0
    max_x = 0
    max_y = 0
    for j in range(cell_size - square_size + 1):
        for i in range(cell_size - square_size + 1):
            s = get_window_sum(i, j, cells, square_size, cache)

            if s > max_value:
                max_value = s
                max_x = i
                max_y = j

    return max_x, max_y, max_value


def get_coordinate_and_size(serial_number):
    cache = {}
    cell_size = 300
    cells = [
        [get_power_level(i, j, serial_number) for i in range(cell_size)]
        for j in range(cell_size)
    ]

    max_value = 0
    max_x = 0
    max_y = 0

    for i in range(300):
        x, y, value = find_max_value(cells, cell_size, i + 1, cache)
        if value > max_value:
            max_value = value
            max_x = x
            max_y = y

    return max_x, max_y, max_value


def get_window_sum(x, y, cells, window_size, cache):
    if (x, y, window_size) in cache:
        return cache[(x, y, window_size)]
    elif window_size == 1:
        return cells[y][x]
    else:
        s = sum([
            cells[j][x + window_size - 1]
            for j in range(y, y + window_size)
        ]) + sum([
            cells[y + window_size - 1][i]
            for i in range(x, x + window_size - 1)
        ]) + get_window_sum(x, y, cells, window_size - 1, cache)
        cache[(x, y, window_size)] = s
        return s
