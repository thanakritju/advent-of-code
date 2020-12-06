def count_answer(answers):
    count = 0
    for group in answers:
        count += len(set("".join(group)))
    return count


def count_answered_by_everyone(answers):
    count = 0
    for group in answers:
        intersections = set(group[0])
        for answer in group[1:]:
            intersections = intersections.intersection(set(answer))
        count += len(intersections)
    return count
