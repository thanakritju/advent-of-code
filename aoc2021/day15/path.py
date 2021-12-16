from heapq import *


def lowest_cost(content, times=1):
    grids = load_data(content, times)
    q = [(0, 0, 0)]
    visited = set()
    while q:
        distance, x, y = heappop(q)
        if x == len(grids[0]) - 1 and y == len(grids) - 1:
            return distance

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if is_valid(x + dx, y + dy, grids, visited):
                visited.add((x+dx, y+dy))
                heappush(q, (distance + grids[y+dy][x+dx], x+dx, y+dy))


def is_valid(x, y, grids, visited):
    return x >= 0 and y >= 0 and x < len(grids[0]) and y < len(grids) and (x, y) not in visited


def load_data(content, times):
    return [
        [(int(char)+i+j) % 10 + (int(char)+i+j) // 10 for i in range(times)
         for char in line]
        for j in range(times) for line in content.splitlines()
    ]
