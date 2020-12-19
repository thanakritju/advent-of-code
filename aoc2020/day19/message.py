import re
import copy


A = "a"
B = "b"
PIPE = "|"


def get_valid_messages(rules, messages):
    rule = get_rule(rules, "0")
    return len([message for message in messages if re.search(f"^{rule}$", message)])


def get_rule(rules, index):
    rules_map = {}
    for line in rules:
        i, rule = line.split(": ")
        rules_map[i] = parse_rule(rule)

    while not is_finish(rules_map):
        for k, v in rules_map.items():
            tokens = [token for token in v if has_number(token)]
            new_v = copy.deepcopy(v)
            for token in tokens:
                token_index = new_v.index(token)
                new_v = new_v[:token_index] + \
                    rules_map[token] + new_v[token_index+1:]
            rules_map[k] = new_v

    return "".join(rules_map[index])


def is_finish(rules_map):
    for v in rules_map.values():
        for token in v:
            if has_number(token):
                return False

    return True


def has_number(token):
    return re.search(r"\d+", token)


def parse_rule(rule):
    if A in rule or B in rule:
        return [rule.replace('"', '')]
    elif PIPE in rule:
        return ["("] + rule.split(" ") + [")"]
    else:
        return rule.split(" ")
