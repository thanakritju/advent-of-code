from typing import Sequence, Tuple, Dict
from collections import Counter
import pprint


StringInput = Sequence[str]
CoordinateList = Sequence[Tuple[int, int]]
Space = Sequence[Sequence[int]]


def biggest_area(coordinates: StringInput) -> int:
    input_list = parse(coordinates)
    max_x = max(list(map(lambda x: x[0], input_list))) + 3
    max_y = max(list(map(lambda x: x[1], input_list))) + 3

    space = create_space(max_x, max_y)

    for row_number, row in enumerate(space):
        for column_number, column in enumerate(row):
            distances = [
                manhattan_distance(
                    condinate[1], condinate[0], column_number, row_number)
                for condinate in input_list
            ]
            space[row_number][column_number] = get_min_index(distances)

    infinite_canidates = get_infinite_canidates(space)
    areas = get_area_for_each_canidates(space)

    return max([area for canidate, area in areas.items() if canidate not in infinite_canidates])


def area_within_distance(coordinates: StringInput, sum_distances: int) -> int:
    input_list = parse(coordinates)
    max_x = max(list(map(lambda x: x[0], input_list))) + 3
    max_y = max(list(map(lambda x: x[1], input_list))) + 3

    space = create_space(max_x, max_y)

    area = 0
    for row_number, row in enumerate(space):
        for column_number, column in enumerate(row):
            distances = [
                manhattan_distance(
                    condinate[1], condinate[0], column_number, row_number)
                for condinate in input_list
            ]
            if (sum(distances) <= 10000):
                area += 1

    return area


def get_infinite_canidates(space: Space) -> Sequence[int]:
    canidates = space[0]
    canidates += space[len(space) - 1]
    canidates += list(map(lambda x: x[0], space))
    canidates += list(map(lambda x: x[len(x) - 1], space))
    return set(canidates)


def get_area_for_each_canidates(space: Space) -> Dict[int, int]:
    area = Counter()
    for row_number, row in enumerate(space):
        for column_number, canidate in enumerate(row):
            area[canidate] += 1
    return area


def get_min_index(distances: Sequence[int]) -> int:
    min_index = min(range(len(distances)), key=distances.__getitem__)
    count = sum([distances[min_index] == distance for distance in distances])
    return min_index + 1 if count == 1 else 0


def manhattan_distance(prev_row: int, prev_col: int, goal_row: int, goal_col: int) -> int:
    return abs(prev_row - goal_row) + abs(prev_col - goal_col)


def parse(coordinates: StringInput) -> CoordinateList:
    return list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), coordinates))


def create_space(width: int, height: int) -> Space:
    return [[0 for column in range(width)] for row in range(height)]


def render_space(space: Space):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(space)
