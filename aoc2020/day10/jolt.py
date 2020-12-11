def get_jolt_differences(jolts):
    jolts = prep_jolts(jolts)
    return count_jolt_diff(jolts)


def prep_jolts(jolts):
    jolts = sorted(jolts)
    out_jolt = max(jolts) + 3
    source_jolt = 0
    jolts.append(out_jolt)
    jolts.insert(0, source_jolt)
    return jolts


def count_jolt_diff(jolts):
    jolt_1 = 0
    jolt_3 = 0
    for jolt_number in range(len(jolts) - 1):
        jolt_diff = jolts[jolt_number + 1] - jolts[jolt_number]
        if jolt_diff == 1:
            jolt_1 += 1
        elif jolt_diff == 3:
            jolt_3 += 1

    return jolt_1, jolt_3


def count_jolt_arrangements(jolts):
    arrangements = 1
    jolts = prep_jolts(jolts)
    last_3_diff = -1
    for jolt_number in range(len(jolts) - 1):
        if jolts[jolt_number + 1] - jolts[jolt_number] == 3:
            sub_list = jolts[last_3_diff + 1:jolt_number + 1]
            print(sub_list)
            sub_list_len = len(sub_list)
            if sub_list_len == 3:
                arrangements *= 2
            elif sub_list_len == 4:
                arrangements *= 4
            elif sub_list_len == 5:
                arrangements *= 7

            last_3_diff = jolt_number

    return arrangements
