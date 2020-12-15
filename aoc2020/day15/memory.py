class Number:
    def __init__(self, turn):
        self.last_turn = turn
        self.second_last_turn = None

    def get_diff(self):
        return self.last_turn - self.second_last_turn

    def add(self, turn):
        self.second_last_turn = self.last_turn
        self.last_turn = turn


class History:
    def __init__(self):
        self.records = dict()
        self.last_spoken_number = None

    def add(self, number, turn):
        try:
            self.records[number].add(turn)
        except:
            self.records[number] = Number(turn)
        self.last_spoken_number = number

    def get_next_number(self):
        try:
            return self.records[self.last_spoken_number].get_diff()
        except:
            return 0


def get_spoken_number(starting_numbers, target_turn):
    starting_numbers = list(map(int, starting_numbers.split(",")))
    turn = 1
    history = History()

    while len(starting_numbers) != 0:
        next_number = starting_numbers.pop(0)
        history.add(next_number, turn)
        turn += 1

    while turn <= target_turn:
        next_number = history.get_next_number()
        history.add(next_number, turn)
        turn += 1

    return history.last_spoken_number
