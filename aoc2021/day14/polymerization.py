from collections import defaultdict


def count_polymerization(content, times):
    bigram, frequency, m = load_data(content)
    print(-1, frequency)
    for _ in range(times):
        bigram, frequency = polymerize(bigram, frequency, m)
        print(_, frequency)

    l = sorted(frequency.items(), key=lambda item: item[1])

    return l[-1][1] - l[0][1]


def polymerize(bigram, frequency, m):
    t = defaultdict(int)
    for k, v in bigram.items():
        if k in m:
            t[k[0]+m[k]] = t[k[0]+m[k]] + v
            t[m[k]+k[1]] = t[m[k]+k[1]] + v
            frequency[m[k]] = frequency[m[k]] + v
    return t, frequency


def load_data(content):
    bigram = defaultdict(int)
    frequency = defaultdict(int)
    frequency[content[0][0]] = 1
    for i in range(1, len(content[0])):
        k = content[0][i-1]+content[0][i]
        bigram[k] = bigram[k] + 1
        frequency[content[0][i]] = frequency[content[0][i]] + 1

    m = {}
    for line in content[1].splitlines():
        k, v = line.split(" -> ")
        m[k] = v

    return bigram, frequency, m
