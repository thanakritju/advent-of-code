from itertools import combinations_with_replacement


def find_weakness(numbers, preamble):
    for index, number in enumerate(numbers):
        if index >= preamble and is_valid(number, numbers[index - preamble:index]):
            return number


def is_valid(number, related_numbers):
    possible_numbers = [
        sum(comb) for comb in combinations_with_replacement(related_numbers, 2)]
    return number not in possible_numbers


def exploit_weakness(numbers, weakness):
    for index, number in enumerate(numbers):
        list_length = 2
        contiguous_list = numbers[index:index + list_length]
        sum_contiguous_list = sum(contiguous_list)
        while True:
            if sum_contiguous_list == weakness:
                return max(contiguous_list) + min(contiguous_list)
            elif sum_contiguous_list > weakness:
                break
            else:
                list_length += 1
                contiguous_list = numbers[index:index + list_length]
                sum_contiguous_list = sum(contiguous_list)
