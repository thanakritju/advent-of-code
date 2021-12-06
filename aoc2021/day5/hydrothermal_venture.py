from collections import defaultdict

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def is_straight(self):
        return self.is_horizontal() or self.is_vertical() or self.is_diagonal()

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_diagonal(self):
        return abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)

    def get_covered_points(self):
        length_x = abs(self.start.x - self.end.x) + 1
        length_y = abs(self.start.y - self.end.y) + 1
        if self.is_vertical():
            if self.start.y > self.end.y:
                return [(self.start.x, self.end.y + i) for i in range(length_y)]
            else:
                return [(self.start.x, self.start.y + i) for i in range(length_y)]

        if self.is_horizontal():
            if self.start.x > self.end.x:
                return [(self.end.x + i, self.start.y) for i in range(length_x)]
            else:
                return [(self.start.x + i, self.start.y) for i in range(length_x)]

        if self.is_diagonal():
            if self.start.x > self.end.x:
                if self.start.y > self.end.y:
                    return [(self.end.x + i, self.end.y + i) for i in range(length_x)]
                else:
                    return [(self.end.x + i, self.end.y - i) for i in range(length_x)]
            else:
                if self.start.y > self.end.y:
                    return [(self.end.x - i, self.end.y + i) for i in range(length_x)]
                else:
                    return [(self.end.x - i, self.end.y - i) for i in range(length_x)]

    def draw_line(self, map):
        if not self.is_straight():
            return
        for point in self.get_covered_points():
            map[point] += 1


def get_overlapped_points(content):
    map = defaultdict(int)
    lines = load_data(content)
    for line in lines:
        if line.is_diagonal():
            continue
        line.draw_line(map)

    return count_items(map)


def get_overlapped_points_with_diagonal(content):
    map = defaultdict(int)
    lines = load_data(content)
    for line in lines:
        line.draw_line(map)

    return count_items(map)


def count_items(map):
    return sum([1 for value in map.values() if value > 1])


def load_data(content):
    lines = []
    for line in content:
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        lines.append(Line(Point(int(x1), int(y1)), Point(int(x2), int(y2))))
    return lines
