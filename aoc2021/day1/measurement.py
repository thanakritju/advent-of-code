def get_number_of_increase_measurement(report):
    previous_record = report[0]
    count = 0
    for each_record in report[1:]:
        if each_record > previous_record:
            count += 1
        previous_record = each_record
    return count


def get_number_of_increase_measurement_in_three_sliding_window(report):
    start_index = 0
    end_index = 2
    report_length = len(report)
    three_measurement = []
    while end_index != report_length:
        three_measurement.append(sum(report[start_index: end_index+1]))
        start_index += 1
        end_index += 1
    return get_number_of_increase_measurement(three_measurement)
