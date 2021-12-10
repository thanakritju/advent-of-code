def power(x, y, serial_number):
    rack_id = x + 10
    return int(str((rack_id * y + serial_number) * rack_id // 100)[-1]) - 5


def get_coordinate(serial_number, ws):
    sums = get_sums(serial_number)

    max_value = 0
    max_x = 0
    max_y = 0

    for j in range(300 - ws):
        for i in range(300 - ws):
            window_sum = sums[j][i] + sums[j + ws][i + ws] - sums[j + ws][i] - sums[j][i + ws]
            if window_sum > max_value:
                max_value = window_sum
                max_x = i
                max_y = j

    return max_x + 1, max_y + 1

def get_coordinate_and_size(serial_number):
    sums = get_sums(serial_number)

    max_value = 0
    max_size = 0
    max_x = 0
    max_y = 0

    for ws in range(1, 300):
        for j in range(300 - ws):
            for i in range(300 - ws):
                window_sum = sums[j][i] + sums[j + ws][i + ws] - sums[j + ws][i] - sums[j][i + ws]
                if window_sum > max_value:
                    max_value = window_sum
                    max_size = ws
                    max_x = i
                    max_y = j

    return max_x + 1, max_y + 1, max_size


def get_sums(serial_number):
    sums = [
        [0 for _ in range(300)]
        for _ in range(300)
    ]

    for j in range(300):
        for i in range(300):
            if i == 0 and j == 0:
                sums[j][i] = power(i, j, serial_number)
            else:
                sums[j][i] = power(i, j, serial_number) + sums[j][i - 1] + sums[j - 1][i] - sums[j - 1][i - 1]

    return sums
