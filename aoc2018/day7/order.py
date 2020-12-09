import re
from typing import Sequence, Tuple
import string
import time


class Task:
    def __init__(self, time_need, name=""):
        self.name = name
        self.start_time = None
        self.time_need = time_need

    def process(self, current_time):
        self.start_time = current_time

    def is_finished(self, current_time):
        return current_time - self.start_time >= self.time_need + string.ascii_uppercase.find(self.name)

    def is_empty(self):
        return self.name == ""


def order(instructions: Sequence[str], worker_number=1, time_need=1) -> str:
    edges = set(map(parse_input, instructions))
    out, time = process_job(edges, worker_number, time_need)
    return "".join(out), time


def process(queue: Sequence[str], out: Sequence[str], edges: Tuple[str, str]) -> Tuple[Sequence[str], Sequence[str]]:
    node = queue.pop(0)
    prerequisites = [edge[0] for edge in edges if node == edge[1]]
    if(all(each in out for each in prerequisites)):
        out.append(node)
        queue += [edge[1] for edge in edges if node ==
                  edge[0] and edge[1] not in queue]
        queue = sorted(queue)
    else:
        queue.append(node)
    return queue, out


def process_job(edges: Tuple[str, str], worker_number: int, time_need: int) -> Sequence[str]:
    out = []
    main_queue = get_first_tasks(edges)
    seconds = 0
    if worker_number == 1:
        while len(main_queue) != 0:
            main_queue, out = process(main_queue, out, edges)
        return out, None
    else:
        empty_tasks = [Task(time_need) for each in range(worker_number)]
        tasks, main_queue = fill_tasks(empty_tasks, main_queue, seconds)
        is_all_done = False
        while len(main_queue) != 0 or not is_all_done:
            main_queue, out, tasks = process_task(
                main_queue, out, tasks, edges, seconds, time_need)
            seconds += 1
            is_all_done = all([task.is_empty() for task in tasks])
            # print(f"out {out}, main_queue {main_queue}, seconds {seconds}")
            time.sleep(0.001)
        return out, seconds - 1


def process_task(main_queue, out, tasks: Sequence[Task], edges, seconds, time_need):
    for i, task in enumerate(tasks):
        prerequisites = [edge[0] for edge in edges if task.name == edge[1]]
        # print(f"worker {i}, task {task.name}, task {task.name}, seconds {seconds}")
        if not task.is_empty() and task.is_finished(seconds) and all(each in out for each in prerequisites):
            out.append(task.name)
            main_queue += get_next_tasks(task, main_queue, tasks, edges, out)
            tasks[i] = Task(time_need)
            main_queue = sorted(main_queue)

    tasks, main_queue = fill_tasks(tasks, main_queue, seconds)
    return main_queue, out, tasks


def get_next_tasks(finished_task, main_queue, tasks, edges, out):
    return [
        edge[1] for edge in edges
        if finished_task.name == edge[0] and
        edge[1] not in main_queue and
        edge[1] not in list(map(lambda x: x.name, tasks)) and
        all(each in out for each in [another_edge[0]
                                     for another_edge in edges if edge[1] == another_edge[1]])
    ]


def get_first_tasks(edges):
    sources = set(map(lambda x: x[0], edges))
    dests = set(map(lambda x: x[1], edges))
    return sorted(list(sources.difference(dests)))


def fill_tasks(tasks, main_queue, seconds):
    for i in range(len(tasks)):
        if tasks[i].is_empty() and len(main_queue) != 0:
            tasks[i].name = main_queue.pop(0)
            tasks[i].process(seconds)
    return tasks, main_queue


def parse_input(instruction: str) -> Tuple[str, str]:
    m = re.search(
        r"Step (?P<source>.) must be finished before step (?P<dest>.) can begin.", instruction)
    return m.group('source'), m.group('dest')
