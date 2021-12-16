
from functools import reduce


class Node:
    def __init__(self):
        self.children = []
        self.literal_value = None
        self.version = None
        self.package_type_id = None
        self.length_type_id = None

    def sum(self):
        return self.version + sum([node.sum() for node in self.children])

    def value(self):
        if self.package_type_id == 0:
            return sum([node.value() for node in self.children])
        if self.package_type_id == 1:
            return reduce((lambda x, y: x * y), [node.value() for node in self.children])
        if self.package_type_id == 2:
            return min([node.value() for node in self.children])
        if self.package_type_id == 3:
            return max([node.value() for node in self.children])
        if self.package_type_id == 4:
            return self.literal_value
        if self.package_type_id == 5:
            return 1 if self.children[0].value() > self.children[1].value() else 0
        if self.package_type_id == 6:
            return 1 if self.children[0].value() < self.children[1].value() else 0
        if self.package_type_id == 7:
            return 1 if self.children[0].value() == self.children[1].value() else 0


class Index:
    def __init__(self):
        self.v = 0

    def next(self, value):
        self.v += value
        return self.v


def decode(encoded):
    node = read_node(hex_to_binary(encoded), Index())
    return node.version, node.package_type_id, node.literal_value, node.length_type_id, len(node.children)


def read_node(binary, index: Index):
    node = Node()
    node.version = int(binary[index.v:index.next(3)], 2)
    node.package_type_id = int(binary[index.v:index.next(3)], 2)

    if node.package_type_id == 4:
        temp = ""
        while True:
            start = binary[index.v]
            temp += binary[index.next(1):index.next(4)]
            if start == "0":
                break
        node.literal_value = int(temp, 2)

    else:
        node.length_type_id = binary[index.next(1)-1]
        if node.length_type_id == "0":
            total_length = int(binary[index.v:index.next(15)], 2)
            start_index = index.v
            while total_length - index.v + start_index > 0:
                node.children.append(read_node(binary, index))
        if node.length_type_id == "1":
            children_numbers = int(binary[index.v:index.next(11)], 2)
            for _ in range(children_numbers):
                node.children.append(read_node(binary, index))

    return node


def hex_to_binary(hexadecimal):
    binary = ""
    for char in hexadecimal:
        binary += bin(int(char, 16))[2:].zfill(4)
    return binary


def sum_of_version_numbers(encoded):
    node = read_node(hex_to_binary(encoded), Index())
    return node.sum()


def value(encoded):
    node = read_node(hex_to_binary(encoded), Index())
    return node.value()
