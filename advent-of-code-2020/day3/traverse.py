

def traverse(patterns, row_move=1, col_move=3):
    forest = create_forest(patterns)
    return find_tree(forest, row_move, col_move)


def create_forest(patterns):
    return [[char for char in row] for row in patterns]


def find_tree(forest, row_move, col_move):
    tree_count = 0
    length = len(forest)
    row_length = len(forest[0])

    if (col_move >= row_move):
        ratio = col_move // row_move
        for row_index in range(1, length):
            if forest[row_index][ratio * row_index % row_length] == '#':
                tree_count += 1
    else:
        ratio = row_move // col_move
        for row_index in range(1, length):
            if row_index % ratio == 0:
                if forest[row_index][int(row_index / ratio) % row_length] == '#':
                    tree_count += 1

    return tree_count
