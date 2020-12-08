import re
import copy


RE_ACTION = r"(?P<action>nop|acc|jmp) (?P<number>[+-]\d+)"


class Action:
    def __init__(self, action_type, number):
        self.type = action_type
        self.number = number


class State:
    def __init__(self, action_list):
        self.acc = 0
        self.pointer = 0
        self.visited_pointers = []
        self.program_length = len(action_list)

    def setPointer(self, new_pointer):
        self.visited_pointers.append(self.pointer)
        self.pointer = new_pointer

    def isCurrentPointerVisited(self):
        return self.pointer in self.visited_pointers

    def isTerminatedCorrectly(self):
        return self.pointer == self.program_length


def run(actions):
    action_list = parse_input(actions)
    state = run_list(action_list)
    return state.acc


def run_list(action_list):
    state = State(action_list)
    while not state.isCurrentPointerVisited() and not state.isTerminatedCorrectly():
        state = dispatch(state, action_list[state.pointer])

    return state


def find_correct_program(actions):
    action_list = parse_input(actions)
    for index, action in enumerate(action_list):
        temp_list = copy.deepcopy(action_list)
        if action.type == "jmp":
            temp_list[index].type = "nop"
            state = run_list(temp_list)
        elif action.type == "nop":
            temp_list[index].type = "jmp"
            state = run_list(temp_list)
        else:
            continue
        if state.isTerminatedCorrectly():
            return state.acc


def dispatch(state, action):
    if action.type == "acc":
        state.acc += action.number
        state.setPointer(state.pointer + 1)
    elif action.type == "jmp":
        state.setPointer(state.pointer + action.number)
    elif action.type == "nop":
        state.setPointer(state.pointer + 1)
    return state


def parse_input(actions):
    return [parse_action(action) for action in actions]


def parse_action(action):
    m = re.search(RE_ACTION, action)
    return Action(m.group("action"), int(m.group("number")))
