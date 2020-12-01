from typing import Sequence


def get_sum_of_two_entries(expense_report: Sequence[int]):
    for index, expense in enumerate(expense_report):
        for another_expense in expense_report[:index]:
            if expense + another_expense == 2020:
                return expense * another_expense


def get_sum_of_three_entries(expense_report: Sequence[int]):
    for index, expense in enumerate(expense_report):
        for another_index, another_expense in enumerate(expense_report[:index]):
            for yet_another_expense in expense_report[:another_index]:
                if expense + another_expense + yet_another_expense == 2020:
                    return expense * another_expense * yet_another_expense
