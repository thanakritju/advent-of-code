def count_paths(content):
    map = load_data(content)
    histories = set()
    dfs(map, "start", [], histories)
    return len(histories)


def dfs(map, node, history, histories):
    history.append(node)
    if node == "end":
        histories.add("".join(history))
        return
    else:
        for each in map[node]:
            if is_big_cave(each) or each not in history:
                dfs(map, each, history.copy(), histories)


def count_paths_v2(content):
    map = load_data(content)
    histories = set()
    for node in map.keys():
        if is_small_cave(node):
            dfs_v2(map, "start", [], histories, node)
    return len(histories)


def dfs_v2(map, node, history, histories, special_small_cave):
    history.append(node)
    if node == "end":
        histories.add("".join(history))
        return
    else:
        for each in map[node]:
            if each == special_small_cave:
                if sum([1 for node in history if node == special_small_cave]) < 2:
                    dfs_v2(map, each, history.copy(),
                           histories, special_small_cave)
            elif is_big_cave(each) or each not in history:
                dfs_v2(map, each, history.copy(),
                       histories, special_small_cave)


def is_big_cave(name):
    return name.isupper()


def is_small_cave(name):
    return name.islower() and name != "start" and name != "end"


def load_data(content):
    d = {}
    for line in content:
        k, v = line.split("-")
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]
        if v in d:
            d[v].append(k)
        else:
            d[v] = [k]
    return d
