import re
from datetime import datetime


SHIFT_CHANGE_ACTION = 'shift_change'
WAKE_ACTION = 'wake'
SLEEP_ACTION = 'sleep'


class Guard:
    def __init__(self, id, time_stamp=None):
        self.id = id
        self.sleep_time_in_minute = 0
        self.last_start_sleep_time_stamp = time_stamp
        self.frequency = dict.fromkeys(range(0, 60), 0)


class State:
    def __init__(self):
        self.all_guards = []
        self.active_guard = None


def guard(actions):
    state = State()
    for action in actions:
        state = reduce_guard(state, action)

    most_sleepy_guard = None
    for guard in state.all_guards:
        if most_sleepy_guard is None:
            most_sleepy_guard = guard
        elif most_sleepy_guard.sleep_time_in_minute < guard.sleep_time_in_minute:
            most_sleepy_guard = guard

    most_frequency = max(most_sleepy_guard.frequency,
                         key=most_sleepy_guard.frequency.get)
    print(most_frequency)
    print(most_sleepy_guard.frequency)

    return most_frequency * most_sleepy_guard.id


def reduce_guard(state, action):
    time_stamp, action_type, guard_id = parse_action(action)
    if action_type == SHIFT_CHANGE_ACTION:

        guard = find_guard(state.all_guards, guard_id)
        if guard == None:
            new_guard = Guard(guard_id, time_stamp)
            state.all_guards.append(new_guard)
            state.active_guard = new_guard
        else:
            state.active_guard = guard

    elif action_type == WAKE_ACTION:

        update_guard(state.active_guard, time_stamp)

    elif action_type == SLEEP_ACTION:

        state.active_guard.last_start_sleep_time_stamp = time_stamp

    return state


def find_guard(all_guards, guard_id):
    for guard in all_guards:
        if guard.id == guard_id:
            return guard
    return None


def update_guard(guard, current_time):
    start_time = guard.last_start_sleep_time_stamp
    guard.sleep_time_in_minute += get_minutes(start_time, current_time)
    for index in range(start_time.minute, start_time.minute + guard.sleep_time_in_minute):
        try:
            guard.frequency[index] += 1
        except:
            pass


def get_minutes(time_stamp, time_stamp_2):
    seconds = (time_stamp_2 - time_stamp).seconds
    return (seconds % 3600) // 60


def parse_action(action):
    m = re.search(r"\[(?P<time_str>.*?)\] (?P<action>.*)", action)
    time_stamp = datetime.strptime(m.group('time_str'), '%Y-%m-%d %H:%M')

    action_type = ''
    guard_id = None

    if m.group('action') == 'wakes up':
        action_type = WAKE_ACTION
    elif m.group('action') == 'falls asleep':
        action_type = SLEEP_ACTION
    else:
        m = re.search(r"Guard #(?P<guard_id>\d+) begins shift", action)
        guard_id = int(m.group('guard_id'))
        action_type = SHIFT_CHANGE_ACTION

    return time_stamp, action_type, guard_id
