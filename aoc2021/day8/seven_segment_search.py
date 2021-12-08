from collections import defaultdict


class SevenSegment:
    #     aaaa
    #    b    c
    #    b    c
    #     dddd
    #    e    f
    #    e    f
    #     gggg

    def __init__(self, patterns):
        self.patterns = patterns
        self.map = {}
        sixs = []
        fives = []
        for code in patterns:
            if len(code) == 3:
                self.map[7] = code
            if len(code) == 2:
                self.map[1] = code
            if len(code) == 4:
                self.map[4] = code
            if len(code) == 7:
                self.map[8] = code
            if len(code) == 6:
                # 6, 9, 0
                sixs.append(code)
            if len(code) == 5:
                # 2, 5, 3
                fives.append(code)

        bd = self.map[4] - self.map[1]
        cf = self.map[1]

        for code in sixs:
            if not bd.issubset(code):
                self.map[0] = code
                sixs.remove(code)
                break

        for code in sixs:
            if cf.issubset(code):
                self.map[9] = code
                sixs.remove(code)
                break

        self.map[6] = sixs[0]

        for code in fives:
            if bd.issubset(code):
                self.map[5] = code
                fives.remove(code)
                break

        for code in fives:
            if cf.issubset(code):
                self.map[3] = code
                fives.remove(code)
                break

        self.map[2] = fives[0]


def search_seven_segment(lines):
    count = 0
    for s, output in parse_data(lines):
        for each in output:
            for k, v in s.map.items():
                if k in [1, 4, 7, 8] and v == each:
                    count += 1
    return count


def get_sum_of_output(lines):
    answer = 0
    for s, output in parse_data(lines):
        temp = ""
        for each in output:
            for k, v in s.map.items():
                if v == each:
                    temp += str(k)
        answer += int(temp)
    return answer


def parse_data(lines):
    for line in lines:
        patterns, output = line.split(" | ")
        s = SevenSegment(map(set, patterns.split(" ")))
        output = map(set, output.split(" "))
        yield s, output
