import math


def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


def cal_fuel(crabs, position):
    return sum(abs(p - position) for p in crabs)


def cheapest_fuel(crabs):
    return cal_fuel(crabs, sorted(crabs)[len(crabs)//2])


def cal_fuel_v2(crabs, position):
    return sum(sum([i + 1 for i in range(abs(p - position))]) for p in crabs)


def cheapest_fuel_v2(crabs):
    avg = int(sum(sorted([c for c in crabs]))//len(crabs))
    return cal_fuel_v2(crabs, avg)
