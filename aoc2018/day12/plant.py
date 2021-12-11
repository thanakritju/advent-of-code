from collections import OrderedDict


def count_plants(content, generations):
    state, rules = load_data(content)
    for _ in range(generations):
        state = process(state, rules)

    return plants(state)


def count_plants_v2(content, generations):
    state, rules = load_data(content)
    for _ in range(150):
        state = process(state, rules)

    count = 0
    for k, v in state.items():
        if v == "#":
            count += generations - 150 + k

    return count


def process(state, rules):
    new_state = OrderedDict()
    start_index = None
    end_index = None

    for index in state.keys():
        if start_index is None:
            start_index = index
        end_index = index
        search_string = get_neighbors(state, index)
        if search_string in rules.keys():
            new_state[index] = rules[search_string]
        else:
            new_state[index] = "."

    for index in [start_index - 2, start_index - 1, end_index + 1, end_index + 2]:
        search_string = get_neighbors(state, index)
        if search_string in rules.keys():
            new_state[index] = rules[search_string]
        else:
            new_state[index] = "."
    return new_state


def get_neighbors(s, i):
    return safe_get(s, i-2) + safe_get(s, i-1) + safe_get(s, i) + safe_get(s, i+1) + safe_get(s, i+2)


def safe_get(s, i):
    if i in s.keys():
        return s[i]
    else:
        return "."


def plants(state):
    return sum([i for i, char in state.items() if char == "#"])


def load_data(content):
    m = {}
    for line in content[1].splitlines():
        k, v = line.split(" => ")
        m[k] = v

    s = OrderedDict()
    for i, char in enumerate(content[0].split(": ")[1]):
        s[i] = char
    return s, m
