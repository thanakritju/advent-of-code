from collections import deque


score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score_map_v2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

delimiters = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

delimiters_rev = {v: k for k, v in delimiters.items()}


def syntax_error_score(navigations):
    answer = 0

    for navigation in navigations:
        _, found = get_corrupted_char(navigation)
        if found:
            answer += score_map[found]

    return answer


def get_corrupted_char(navigation):
    q = deque()

    for char in navigation:
        if char in delimiters.keys():
            if q[-1] == delimiters[char]:
                q.pop()
            else:
                return delimiters_rev[q[-1]], char
        else:
            q.append(char)

    return None, None


def incomplete_score(navigations):
    scores = []

    for navigation in navigations:
        chars = get_incomplete_chars(navigation)
        if chars:
            score = 0
            for char in chars:
                score = score * 5 + score_map_v2[char]
            scores.append(score)

    return sorted(scores)[len(scores)//2]


def get_incomplete_chars(navigation):
    q = deque()

    answer = ""
    for char in navigation:
        if char in delimiters.keys():
            if q[-1] == delimiters[char]:
                q.pop()
            else:
                return ""
        else:
            q.append(char)
    while q:
        answer += delimiters_rev[q.pop()]

    return answer
