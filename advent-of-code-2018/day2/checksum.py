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

def get_common_id(box_ids):
    return "fgij"