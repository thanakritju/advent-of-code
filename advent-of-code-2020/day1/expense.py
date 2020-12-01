def get_sum_of_two_entries(expense_report):
    length = len(expense_report)
    for index in range(length):
        for another in range(index + 1, length):
            if expense_report[index] + expense_report[another] == 2020:
                return expense_report[index] * expense_report[another]


def get_sum_of_three_entries(expense_report):
    length = len(expense_report)
    for index in range(length):
        for another in range(index + 1, length):
            for yet_another in range(index + 2, length):
                if expense_report[index] + expense_report[another] + expense_report[yet_another] == 2020:
                    return expense_report[index] * expense_report[another] * expense_report[yet_another]
