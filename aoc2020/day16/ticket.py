import functools


def get_error_rate(content):
    ranges, my_tickets, nearby_tickets = parse_input(content)
    all_ranges = functools.reduce(lambda a, b: a + b, ranges)
    all_nearby_tickets = functools.reduce(lambda a, b: a + b, nearby_tickets)
    error_sum = 0
    for nearby_ticket in all_nearby_tickets:
        if nearby_ticket not in all_ranges:
            error_sum += nearby_ticket
    return error_sum


def get_multiply(content):
    ranges, my_tickets, nearby_tickets = parse_input(content)

    sets = None
    for tickets in nearby_tickets:
        out_sets = [number_in_ranges(ticket, ranges) for ticket in tickets]

        if not any([out == set() for out in out_sets]):
            if sets is None:
                sets = out_sets
            else:
                sets = merge_sets(sets, out_sets)

    orders = [-1 for ticket in my_tickets]
    while any([order == -1 for order in orders]):
        for i, each in enumerate(sets):
            each = [n for n in list(each) if n not in orders]
            if len(each) == 1:
                orders[i] = each[0]

    mul = 1
    for i, order in enumerate(orders):
        if order in range(0, 6):
            print(i, order, my_tickets[i])
            mul *= my_tickets[i]

    return mul


def merge_sets(sets1, sets2):
    return [
        each_set.intersection(sets2[i])
        for i, each_set in enumerate(sets1)
    ]


def number_in_ranges(number, ranges):
    out = set()
    for i, r in enumerate(ranges):
        if number in r:
            out.add(i)
    return out


def parse_input(content):
    ranges_str, my_tickets_str, nearby_tickets_str = content.split("\n\n")
    ranges = []
    for each_range in ranges_str.splitlines():
        range_1, range_2 = each_range.split(": ")[1].split(" or ")
        range_1_lower, range_1_upper = map(int, range_1.split("-"))
        range_2_lower, range_2_upper = map(int, range_2.split("-"))
        ranges.append(
            list(range(range_1_lower, range_1_upper + 1)) +
            list(range(range_2_lower, range_2_upper + 1))
        )
    my_tickets = []
    for tickets in my_tickets_str.splitlines()[1:]:
        my_tickets += list(map(int, tickets.split(",")))
    nearby_tickets = []
    for tickets in nearby_tickets_str.splitlines()[1:]:
        nearby_tickets.append(list(map(int, tickets.split(","))))
    return ranges, my_tickets, nearby_tickets
