def checksum(box_ids):
    dicts = list(map(transform_to_dict, box_ids))
    number_twice_boxes = len(get_twice_duplicate_boxes(dicts))
    number_triple_boxes = len(get_triple_duplicate_boxes(dicts))
    return number_twice_boxes * number_triple_boxes


def get_twice_duplicate_boxes(dicts):
    return list(filter(lambda my_dict: 2 in my_dict.values(), dicts))


def get_triple_duplicate_boxes(dicts):
    return list(filter(lambda my_dict: 3 in my_dict.values(), dicts))


def transform_to_dict(my_string):
    my_string_dict = dict()
    for char in my_string:
        if char not in my_string_dict.keys():
            my_string_dict[char] = 1
        else:
            my_string_dict[char] += 1
    return my_string_dict


def is_close(first_string, second_string):
    number_of_differ = 0
    for index in range(len(first_string)):
        if first_string[index] != second_string[index]:
            number_of_differ += 1
        if number_of_differ == 2:
            return False
    return True


def drop_duplicate(first_string, second_string):
    out_string = ""
    for index in range(len(first_string)):
        if first_string[index] == second_string[index]:
            out_string += first_string[index]
    return out_string


def get_common_id(box_ids):
    for index in range(len(box_ids)):
        for another_index in range(index + 1, len(box_ids)):
            if is_close(box_ids[index], box_ids[another_index]):
                return drop_duplicate(box_ids[index], box_ids[another_index])
    return ""
