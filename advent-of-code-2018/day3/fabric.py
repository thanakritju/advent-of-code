import re


def get_overlap(fabrics):
    intersections = set()
    fabrics_set = list(map(extract_input, fabrics))
    length = len(fabrics)
    for index in range(length):
        for another_index in range(index + 1, length):
            intersections.update(get_intersection(
                fabrics_set[index], fabrics_set[another_index]))
    return len(intersections)


def is_overlap(fabric, another_fabric):
    return bool(get_intersection(extract_input(fabric), extract_input(another_fabric)))


def get_intersection(fabric, another_fabric):
    return fabric.intersection(another_fabric)


def extract_input(fabric):
    m = re.search(
        r"#\d+ @ (?P<x_start>\d+),(?P<y_start>\d+): (?P<width>\d+)x(?P<height>\d+)", fabric)
    fabric_set = set()
    x_start, y_start, width, height = int(m.group('x_start')), int(
        m.group('y_start')), int(m.group('width')), int(m.group('height'))
    for x_index in range(width):
        for y_index in range(height):
            fabric_set.add((x_start + x_index, y_start + y_index))

    return fabric_set
