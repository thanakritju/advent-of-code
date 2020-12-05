import re


def get_seat_location(seat):
    rows, cols = parse_input(seat)
    row = int("".join(["0" if char == "F" else "1" for char in rows]), 2)
    col = int("".join(["0" if char == "L" else "1" for char in cols]), 2)
    return row, col


def parse_input(seat):
    rows = seat[0:7]
    cols = seat[7:10]
    return rows, cols


def get_missing_id(seats):
    seats = set(map(get_seat_id, seats))
    all_seats = set(range(min(seats), max(seats)))
    return list(all_seats - seats)[0]


def get_seat_id(seat):
    row, col = get_seat_location(seat)
    return 8 * row + col
