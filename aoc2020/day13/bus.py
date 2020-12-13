def get_earliest_bus(bus_time):
    target_timestamp, bus_times = parse_input(bus_time)
    earliest_bus_time = float('inf')
    earliest_bus_id = None
    for bus_time in bus_times:
        minute_to_wait = bus_time - target_timestamp % bus_time
        if minute_to_wait < earliest_bus_time:
            earliest_bus_time = minute_to_wait
            earliest_bus_id = bus_time

    return earliest_bus_time * earliest_bus_id


def parse_input(bus_time):
    return int(bus_time[0]), list(map(int, filter(lambda x: x.isdigit(), bus_time[1].split(","))))


def get_earliest_time(bus_time):
    bus_time = bus_time.split(",")
    bus_list = []
    for bus_index, bus_id in enumerate(bus_time):
        if bus_id != 'x':
            bus_list.append((int(bus_id) - bus_index, int(bus_id)))
    return chinese_remainder_theorem(bus_list)


def chinese_remainder_theorem(bus_list):
    x, m = bus_list[0]
    for each in bus_list[1:]:
        x_2, m_2 = each
        temp1 = modinv(m_2, m) * x * m_2 + modinv(m, m_2) * x_2 * m
        temp2 = m * m_2
        x = temp1 % temp2
        m = temp2

    return x


def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m
