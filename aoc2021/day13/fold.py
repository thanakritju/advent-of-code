from pprint import PrettyPrinter


def fold(content, times):
    coordinates, fold_instructions = load_data(content)

    for i in range(times):
        coordinates = process_fold(coordinates, fold_instructions[i])

    return len(coordinates)


def print_fold(content, times):
    coordinates, fold_instructions = load_data(content)

    for i in range(times):
        coordinates = process_fold(coordinates, fold_instructions[i])

    arrays = ["".join(
        ['#' if (i, j) in coordinates else '.' for i in range(40)]) for j in range(6)]

    pp = PrettyPrinter(indent=2)
    pp.pprint(arrays)

    return True


def process_fold(coordinates, fold_instruction):
    new_coordinates = set()

    if fold_instruction[0] == 0:
        y = fold_instruction[1]
        for i, j in coordinates:
            if j > y:
                new_coordinates.add((i, 2*y-j))
            else:
                new_coordinates.add((i, j))

    else:
        x = fold_instruction[0]
        for i, j in coordinates:
            if i > x:
                new_coordinates.add((2*x-i, j))
            else:
                new_coordinates.add((i, j))

    return new_coordinates


def load_data(content):
    coordinates = set()
    for coordinate in content[0].splitlines():
        x, y = coordinate.split(",")
        coordinates.add((int(x), int(y)))

    fold_instructions = []
    for each in content[1].splitlines():
        _, temp = each.split("fold along ")
        axis, value = temp.split("=")
        if axis == "x":
            fold_instructions.append((int(value), 0))
        else:
            fold_instructions.append((0, int(value)))

    return coordinates, fold_instructions
