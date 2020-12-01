import string


def react_polymer(polymer: str):
    lasted_polymer = process_polymer(polymer)
    while True:
        polymer_out = process_polymer(polymer)
        if lasted_polymer == lasted_polymer:
            break

    return lasted_polymer


def process_polymer(polymer: str):
    polymer_out = ""
    for char in polymer:
        if polymer_out == "":
            polymer_out += char
            continue
        if is_reacted(char, polymer_out[-1]):
            polymer_out = polymer_out[:-1]
        else:
            polymer_out += char

    return polymer_out


def is_reacted(char: str, another_char: str):
    index_lowercase = get_index_lowercase(char)
    if index_lowercase >= 0:
        return get_index_uppercase(another_char) == index_lowercase
    return get_index_uppercase(char) == get_index_lowercase(another_char)


def get_index_lowercase(char: str):
    return string.ascii_lowercase.find(char)


def get_index_uppercase(char: str):
    return string.ascii_uppercase.find(char)


def optimized_react_polymer(polymers: str):
    reacted_polymers = react_polymer(polymers)
    smallest_polymers_length = len(reacted_polymers)
    for alphabatic_index in range(26):
        remaining_polymers = remove_units(reacted_polymers, alphabatic_index)
        polymers_length = len(react_polymer(remaining_polymers))
        if polymers_length < smallest_polymers_length:
            smallest_polymers_length = polymers_length

    return smallest_polymers_length


def remove_units(polymer: str, alphabatic_index: int):
    polymer = polymer.replace(string.ascii_uppercase[alphabatic_index], '')
    return polymer.replace(string.ascii_lowercase[alphabatic_index], '')
