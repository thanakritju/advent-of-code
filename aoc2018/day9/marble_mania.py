class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        new_node = Node(0)
        new_node.next = new_node
        new_node.prev = new_node
        self.head = new_node

    def add_node_counter_clockwise(self, value):
        new_node = Node(value)
        new_node.prev = self.head.next
        new_node.next = self.head.next.next

        self.head.next = new_node
        new_node.next.prev = new_node
        self.head = new_node

    def remove_seventh_node_clockwise(self):
        seventh = self.head.prev.prev.prev.prev.prev.prev.prev
        sixth = seventh.next
        eight = seventh.prev

        sixth.prev = eight
        eight.next = sixth
        return seventh.data

    def print(self):
        start = self.head.data
        head = self.head
        while True:
            print(head.data, end=" -> ")
            head = head.next
            if head.data == start:
                break


def get_high_score(players, last_marble_worth):
    linked_list = CircularLinkedList()

    current_marble_worth = 0
    current_player = 0
    score = [0 for _ in range(players + 1)]

    while True:
        if current_marble_worth % 23 == 0:
            score[current_player] += current_marble_worth + \
                linked_list.remove_seventh_node_clockwise()
        if current_marble_worth == last_marble_worth:
            break
        current_marble_worth += 1
        linked_list.add_node_counter_clockwise(current_marble_worth)
        current_player = (current_player + 1) % players

    linked_list.print()
    return max(score)


print(get_high_score(9, 10))
