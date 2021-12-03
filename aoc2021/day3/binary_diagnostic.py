def get_diagnostic(binarys):
    length_of_binary = len(binarys[0])
    length_of_binarys = len(binarys)
    gamma = ""
    epsilon = ""
    for index in range(length_of_binary):
        s = sum([int(binary[index]) for binary in binarys])
        if s > length_of_binarys / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def get_diagnostic_v2(binarys):
    oxgens = binarys
    co2s = binarys
    length_of_binary = len(binarys[0])
    length_of_binarys = len(binarys)

    for index in range(length_of_binary):
        if len(oxgens) == 1:
            break
        ones, zeros = separate_the_binarys(oxgens, index)

        if len(ones) == len(zeros):
            oxgens = ones
        elif len(ones) > len(zeros):
            oxgens = ones
        else:
            oxgens = zeros

    for index in range(length_of_binary):
        if len(co2s) == 1:
            break
        ones, zeros = separate_the_binarys(co2s, index)

        if len(ones) == len(zeros):
            co2s = zeros
        elif len(ones) > len(zeros):
            co2s = zeros
        else:
            co2s = ones

    return int(oxgens[0], 2) * int(co2s[0], 2)


def separate_the_binarys(binarys, index):
    ones = [binary for binary in binarys if binary[index] == "1"]
    zeros = [binary for binary in binarys if binary[index] == "0"]
    return ones, zeros
