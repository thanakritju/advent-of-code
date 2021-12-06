from collections import defaultdict


def get_lanternfish(lanternfishs, days):
    set_fish = defaultdict(int)
    for each_fish in lanternfishs:
        set_fish[each_fish] += 1

    for _ in range(days):
        set_fish = update_fish(set_fish)

    return sum([value for _, value in set_fish.items()])


def update_fish(set_fish):
    new_set = defaultdict(int)
    for key, value in set_fish.items():
        if key == 0:
            new_set[6] += value
            new_set[8] += value
        else:
            new_set[key - 1] += value

    return new_set
