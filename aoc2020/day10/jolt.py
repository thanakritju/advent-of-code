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
        jolt_diif = jolts[jolt_number + 1] - jolts[jolt_number]
        if jolt_diif == 1:
            jolt_1 += 1
        elif jolt_diif == 3:
            jolt_3 += 1

    return jolt_1, jolt_3


def count_jolt_arrangements(jolts):
    arrangements = 1
    jolts = prep_jolts(jolts)
    
    return 0