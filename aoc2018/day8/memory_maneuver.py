class Node:
    def __init__(self, parent=None):
        self.children = []
        self.metadata_entries = []
        self.parent = parent
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_metadata(self, entry):
        self.metadata_entries.append(entry)


def get_sum_of_all_metadata_entries(records):
    current_metadata_entry = 0
    current_childrens = []
    current_node = Node()
    n = len(records)
    index = 0

    while index != n:
        if current_metadata_entry == 0:
            current_childrens.append(records[index])
            current_metadata_entry = records[index+1]

            index += 2
        else:
            current_node.add_metadata(records[index])

            index += 1
            current_metadata_entry -= 1
