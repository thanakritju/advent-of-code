def get_lanternfish(lanternfishs, days):
    set_fish = {}
    for each_fish in lanternfishs:
        add_item_in_set(set_fish, each_fish)

    for _ in range(days):
        set_fish = update_fish(set_fish)

    return sum([value for _, value in set_fish.items()])


def update_fish(set_fish):
    new_set = {}
    for key, value in set_fish.items():
        if key == 0:
            add_item_in_set(new_set, 6, value)
            add_item_in_set(new_set, 8, value)
        else:
            add_item_in_set(new_set, key - 1, value)

    return new_set


def add_item_in_set(s, k, v=1):
    if k in s:
        s[k] += v
    else:
        s[k] = v
