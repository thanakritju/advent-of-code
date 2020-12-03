import re


def get_overlap(fabrics):
    fabrics_set = transform_to_set(fabrics)
    return len(get_all_intersections(fabrics_set))


def transform_to_set(fabrics):
    return list(map(extract_input, fabrics))


def get_all_intersections(fabrics_set):
    intersection_dict = dict()
    for fabric_set in fabrics_set:
        for coordinate in fabric_set:
            try:
                intersection_dict[coordinate] += 1
            except KeyError:
                intersection_dict[coordinate] = 1

    return set([k for (k, v) in intersection_dict.items() if v > 1])


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


def get_the_isolate_id(fabrics):
    fabrics_set = transform_to_set(fabrics)
    intersections = get_all_intersections(fabrics_set)

    for number, each_fabric in enumerate(fabrics_set):
        if not bool(intersections.intersection(each_fabric)):
            return number + 1

    return -1
