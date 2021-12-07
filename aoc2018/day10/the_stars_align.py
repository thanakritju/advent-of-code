import re
import pprint


class Star:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy


def process(content, times):
    stars = read_data(content)
    update(stars, times)
    print_positions(stars)


def update(stars, times):
    for star in stars:
        for _ in range(times):
            star.update()


def read_data(content):
    lines = list(map(str, content.splitlines()))
    stars = set()

    for line in lines:
        m = re.search(
            r"position=<(?P<position>.*)> velocity=<(?P<velocity>.*)>", line)
        px, py = m.group('position').split(",")
        vx, vy = m.group('velocity').split(",")
        stars.add(Star(int(px), int(py), int(vx), int(vy)))

    return stars


def print_positions(stars):
    s = [(star.x, star.y) for star in stars]
    xs = [star.x for star in stars]
    ys = [star.y for star in stars]
    max_x = max(xs) + 2
    min_x = min(xs) - 2
    max_y = max(ys) + 2
    min_y = min(ys) - 2
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(["".join(["#" if (i, j) in s else "." for i in range(min_x, max_x)])
              for j in range(min_y, max_y)])


with open("aoc2018/day10/sample.txt", "r") as f:
    process(f.read(), 3)


with open("aoc2018/day10/input.txt", "r") as f:
    process(f.read(), 10081)

# 10078 90 39
# 10079 80 29
# 10080 70 19
# 10081 61 9
# 10082 68 19
# 10083 76 29
# 10084 85 39
# 10085 94 49
