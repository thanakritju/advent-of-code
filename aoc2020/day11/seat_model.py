import copy


def count_seat(seats, model):
    seats = parse_seats(seats)
    while True:
        seats, is_the_same = run_model(seats, model)
        if is_the_same:
            break
    return sum(row.count('#') for row in seats)


def run_model(seats, model):
    is_the_same = True
    new_seats = []
    for row_index, row in enumerate(seats):
        for col_index, seat in enumerate(row):
            new_seat = model(seat, seats, row_index, col_index)
            new_seats.append((new_seat, row_index, col_index))
            if seat != new_seat:
                is_the_same = False

    for new_seat, row_index, col_index in new_seats:
        seats[row_index][col_index] = new_seat

    return seats, is_the_same


def get_new_seat(seat, seats, row_index, col_index):
    adj = list(get_adj(seat, seats, row_index, col_index))
    if seat == 'L':
        if adj.count('#') == 0:
            return '#'
    elif seat == '#':
        if adj.count('#') >= 4:
            return 'L'
    return seat


def get_new_seat_v2(seat, seats, row_index, col_index):
    adj = list(get_first_items(seat, seats, row_index, col_index))
    if seat == 'L':
        if adj.count('#') == 0:
            return '#'
    elif seat == '#':
        if adj.count('#') >= 5:
            return 'L'
    return seat


def get_first_items(seat, seats, row_index, col_index):
    directions = [(i, j) for i in (-1, 0, 1)
                  for j in (-1, 0, 1) if not (i == j == 0)]
    max_x = len(seats[0])
    max_y = len(seats)
    items = []
    for dx, dy in directions:
        ratio = 1
        while True:
            new_dx, new_dy = ratio * dx, ratio * dy
            if 0 <= col_index + new_dx < max_x and 0 <= row_index + new_dy < max_y:
                if seats[row_index + new_dy][col_index + new_dx] != '.':
                    items.append(seats[row_index + new_dy][col_index + new_dx])
                    break
            else:
                break
            ratio += 1

    return items


def get_adj(seat, seats, row_index, col_index):
    adjacency = [(i, j) for i in (-1, 0, 1)
                 for j in (-1, 0, 1) if not (i == j == 0)]
    max_x = len(seats[0])
    max_y = len(seats)
    for dx, dy in adjacency:
        if 0 <= col_index + dx < max_x and 0 <= row_index + dy < max_y:
            yield seats[row_index + dy][col_index + dx]


def parse_seats(seats):
    return [list(seat) for seat in seats]
