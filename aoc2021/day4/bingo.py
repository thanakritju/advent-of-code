class BingoBoard:
    def __init__(self, rows):
        self.r = rows
        self.m = [
            [False for _ in range(5)]
            for _ in range(5)
        ]
        self.last_number = None
        self.won = False

    def is_bingo(self):
        horizontal = any([all(row) for row in self.m])
        vertical = any([all([row[i] for row in self.m]) for i in range(5)])
        if horizontal or vertical:
            self.won = True
            return True
        else:
            return False

    def mark_number(self, drawn_number):
        for j, row in enumerate(self.r):
            for i, number in enumerate(row):
                if number == drawn_number:
                    self.m[j][i] = True
                    self.last_number = drawn_number

    def score(self):
        s = 0
        for j, row in enumerate(self.r):
            for i, number in enumerate(row):
                if not self.m[j][i]:
                    s += number
        return s * self.last_number


def get_final_score(content):
    numbers, bingo_boards = load_data(content)

    for number in numbers:
        for board in bingo_boards:
            board.mark_number(number)
            if board.is_bingo():
                return board.score()


def get_final_score_for_last_board(content):
    numbers, bingo_boards = load_data(content)
    count = 0
    numbers_of_boards = len(bingo_boards)

    for number in numbers:
        for board in bingo_boards:
            if board.won:
                continue
            board.mark_number(number)
            if board.is_bingo():
                count += 1
            if count == numbers_of_boards:
                return board.score()


def load_data(content):
    numbers = list(map(int, content[0].split(",")))
    bingo_boards = [
        BingoBoard([
            list(map(int, row.split()))
            for row in board.splitlines()
        ])
        for board in content[1:]
    ]
    return numbers, bingo_boards
