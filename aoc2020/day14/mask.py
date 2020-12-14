from itertools import product


def get_mask_results(inputs):
    mask = None
    results = dict()
    for record in inputs:
        first, second = record.split(" = ")
        if first == "mask":
            mask = second
        else:
            number = custom_mask(mask, int_to_bin(int(second)))
            address = parse_address(first)
            results[address] = int(number, 2)
    return results


def get_mask_results_v2(inputs):
    mask = None
    results = dict()
    for record in inputs:
        first, second = record.split(" = ")
        if first == "mask":
            mask = second
        else:
            value = int(second)
            output_with_floating = custom_mask_v2(
                mask, int_to_bin(parse_address(first)))
            for address in generate_possible_numbers(output_with_floating):
                results[int(address, 2)] = value
    return results


def parse_address(record):
    return int(record.split("[")[1].replace("]", ""))


def int_to_bin(number):
    return bin(number)[2:].zfill(36)


def custom_mask(mask, bin_number):
    return "".join([
        custom_operation(mask[i], bin_number[i])
        for i in range(len(mask))
    ])


def generate_possible_numbers(number_with_floating):
    floating = number_with_floating.count("X")
    for mask in product(*[["0", "1"]]*floating):
        out = number_with_floating
        for item in mask:
            out = out.replace("X", item, 1)
        yield out


def custom_mask_v2(mask, bin_number):
    return "".join([
        custom_operation_v2(mask[i], bin_number[i])
        for i in range(len(mask))
    ])


def custom_operation(mask_char, number_char):
    if mask_char == "X":
        return number_char
    else:
        return mask_char


def custom_operation_v2(mask_char, number_char):
    if mask_char == "X":
        return "X"
    elif mask_char == "1":
        return "1"
    else:
        return number_char
