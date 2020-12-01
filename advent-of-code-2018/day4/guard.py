import re
from datetime import datetime


class Guard:
    def __init__(self, id):
        self.id = id
        self.is_active = False
        self.work_time = 0


def guard(actions):
    state = None
    for action in actions:
        state = reduce_guard(state, action)
    return 0


def reduce_guard(state, action):
    time_stamp, action_type, guard_id = parse_action(action)
    return state


def parse_action(action):
    m = re.search(r"\[(?P<time_str>.*?)\] (?P<action>.*)", action)
    time_stamp = datetime.strptime(m.group('time_str'), '%Y-%m-%d %H:%M')

    action_type = ''
    guard_id = None

    if m.group('action') == 'wakes up':
        action_type = 'wake'
    elif m.group('action') == 'falls asleep':
        action_type = 'sleep'
    else:
        m = re.search(r"Guard #(?P<guard_id>\d+) begins shift", action)
        guard_id = int(m.group('guard_id'))
        action_type = 'shift_change'

    return time_stamp, action_type, guard_id
