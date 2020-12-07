import re


RE_BAG_RECORD = r"^(?P<bag_parent>.*?) contain (?P<bag_child>no other bags|.*?).$"
RE_BAG = r"^ ?(?P<bag_number>\d*)? ?(?P<bag_key>.*?) bags?$"


def count_bag(bags, bag_key):
    adjacency_matrix, vertices = parse_input(bags)
    bags = set()
    queue = [list(vertices).index(bag_key)]
    while (len(queue) != 0):
        node = queue.pop(0)
        for row_number, row in enumerate(adjacency_matrix):
            if row[node] > 0:
                queue.append(row_number)
                bags.add(row_number)

    return len(bags)


def get_all_bags(bags, bag_key):
    adjacency_matrix, vertices = parse_input(bags)
    return get_bags_recursive(adjacency_matrix, list(vertices).index(bag_key))


def get_bags_recursive(adjacency_matrix, bag_key):
    if sum(adjacency_matrix[bag_key]) == 0:
        return 0
    return sum([
        bag * (1 + get_bags_recursive(adjacency_matrix, bag_key))
        for bag_key, bag in enumerate(adjacency_matrix[bag_key])
        if bag != 0])


def parse_input(bags):
    bag_map = dict()
    for bag in bags:
        bag_parent_key, bag_children = parse_string_input(bag)
        bag_map[bag_parent_key] = bag_children

    vertices = bag_map.keys()
    vertices_length = len(vertices)
    adjacency_matrix = [
        [
            bag_map[row_vertice][col_vertice]
            if col_vertice in bag_map[row_vertice]
            else 0
            for col_vertice in vertices
        ]
        for row_vertice in vertices
    ]

    return adjacency_matrix, vertices


def parse_string_input(bag_record):
    m = re.search(RE_BAG_RECORD, bag_record)
    bag_parent, bag_child = m.group("bag_parent"), m.group("bag_child")
    bag_parent_key = extract_bag(bag_parent)[0]
    bag_children_dict = dict()
    if bag_child != "no other bags":
        bag_children = list(
            map(lambda x: extract_bag(x), bag_child.split(",")))
        for child in bag_children:
            bag_children_dict[child[0]] = child[1]
    return bag_parent_key, bag_children_dict


def extract_bag(bag_string):
    m = re.search(RE_BAG, bag_string)
    key = m.group("bag_key")
    number = m.group("bag_number")
    if number == "":
        return key, None
    return key, int(number)
