class Node:
    def __init__(self):
        self.children = []
        self.metadata_entries = []

    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, entry):
        self.metadata_entries.append(entry)

    def sum(self):
        return sum(self.metadata_entries) + sum([child.sum() for child in self.children])

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata_entries)
        else:
            return sum([self.children[each - 1].value() for each in self.metadata_entries if each <= len(self.children)])


class Index:
    def __init__(self):
        self.value = -1

    def next(self):
        self.value += 1
        return self.value


def get_sum_of_all_metadata_entries(records):
    index = Index()
    node = read_node(records, index)
    return node.sum()


def get_sum_of_all_metadata_entries_v2(records):
    index = Index()
    node = read_node(records, index)
    return node.value()


def read_node(numbers, index):
    node = Node()
    children = numbers[index.next()]
    metadata = numbers[index.next()]

    for _ in range(children):
        node.add_child(read_node(numbers, index))

    for _ in range(metadata):
        node.add_metadata(numbers[index.next()])

    return node
