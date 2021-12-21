from functools import lru_cache


def play(p1_position, p2_position):
    p1_score, p2_score = 0, 0
    die_value = 1
    die_count = 0
    while True:

        p1_position, die_value, die_count = update(
            p1_position, die_value, die_count)
        p1_score += p1_position
        if p1_score >= 1000:
            break

        p2_position, die_value, die_count = update(
            p2_position, die_value, die_count)
        p2_score += p2_position
        if p2_score >= 1000:
            break

    return die_count * min((p1_score, p2_score))


@lru_cache(maxsize=None)
def play_quantum(p1_position, p1_score, p2_position, p2_score):
    w1, w2 = 0, 0
    p1 = p1_position
    s1 = p1_score
    for s in [x+y+z for x in (1, 2, 3) for y in (1, 2, 3) for z in (1, 2, 3)]:
        p1_position = (p1 + s - 1) % 10 + 1
        p1_score = s1 + p1_position
        if p1_score >= 21:
            w1 += 1
        else:
            r2, r1 = play_quantum(p2_position, p2_score, p1_position, p1_score)
            w1, w2 = w1+r1, w2+r2
    return w1, w2


def update(position, die_value, die_count):
    s, die_value = update_die(die_value)
    new_position = position + s
    while new_position > 10:
        new_position = new_position - 10
    return new_position, die_value, die_count + 3


def update_die(die_value):
    s = 0
    for _ in range(3):
        s += die_value
        die_value += 1
        if die_value == 101:
            die_value = 1
    return s, die_value
