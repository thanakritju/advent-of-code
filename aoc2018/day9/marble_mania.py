from collections import deque, defaultdict


def get_high_score(players, last_marble_worth):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble_worth + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0
