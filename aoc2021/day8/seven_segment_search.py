from collections import defaultdict


def search_seven_segment(lines):
    count = 0
    for patterns, output in parse_data(lines):
        for each in output:
            for k, v in patterns.items():
                if k in [1, 4, 7, 8] and v == each:
                    count += 1
    return count


def get_sum_of_output(lines):
    answer = 0
    for patterns, output in parse_data(lines):
        temp = ""
        for each in output:
            for k, v in patterns.items():
                if v == each:
                    temp += str(k)
        answer += int(temp)
    return answer


def parse_data(lines):
    for line in lines:
        patterns, output = line.split(" | ")
        patterns = calculate(map(set, patterns.split(" ")))
        output = map(set, output.split(" "))
        yield patterns, output


def calculate(patterns):
    #     aaaa
    #    b    c
    #    b    c
    #     dddd
    #    e    f
    #    e    f
    #     gggg

    map = {}
    sixs = []
    fives = []
    for code in patterns:
        length = len(code)
        if length == 3:
            map[7] = code
        if length == 2:
            map[1] = code
        if length == 4:
            map[4] = code
        if length == 7:
            map[8] = code
        if length == 6:
            # 6, 9, 0
            sixs.append(code)
        if length == 5:
            # 2, 5, 3
            fives.append(code)

    bd = map[4] - map[1]
    cf = map[1]

    for code in sixs:
        if not bd.issubset(code):
            map[0] = code
            sixs.remove(code)
            break

    for code in sixs:
        if cf.issubset(code):
            map[9] = code
            sixs.remove(code)
            break

    map[6] = sixs[0]

    for code in fives:
        if bd.issubset(code):
            map[5] = code
            fives.remove(code)
            break

    for code in fives:
        if cf.issubset(code):
            map[3] = code
            fives.remove(code)
            break

    map[2] = fives[0]

    return map
