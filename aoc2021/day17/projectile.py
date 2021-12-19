def highest_y(content):
    min_x, max_x, min_y, max_y = load_data(content)

    max_height = 0
    for vx in range(0, max_x+1):
        for vy in range(min_y, 200):
            local_max_height, _ = get_highest_y(
                vx, vy, min_x, max_x, min_y, max_y)
            if local_max_height > max_height:
                max_height = local_max_height

    return max_height


def get_all_initial_velocities(content):
    min_x, max_x, min_y, max_y = load_data(content)

    s = set()
    for vx in range(0, max_x+1):
        for vy in range(min_y, 200):
            _, is_hit_target = get_highest_y(
                vx, vy, min_x, max_x, min_y, max_y)
            if is_hit_target:
                s.add((vx, vy))

    return len(s)


def get_highest_y(vx, vy, min_x, max_x, min_y, max_y):
    x, y = (0, 0)
    highest_y = 0
    is_hit_target = False
    while True:
        if hit_target(x, min_x, max_x, y, min_y, max_y):
            is_hit_target = True
            break
        if x > max_x or y < min_y:
            break
        if y > highest_y:
            highest_y = y
        x, y, vx, vy = process(x, y, vx, vy)

    return highest_y if is_hit_target else 0, is_hit_target


def hit_target(x, min_x, max_x, y, min_y, max_y):
    return min_x <= x <= max_x and min_y <= y <= max_y


def process(x, y, vx, vy):
    new_vx = vx
    if vx > 0:
        new_vx -= 1

    return x+vx, y+vy, new_vx, vy-1


def load_data(content):
    x, y = content.split("target area: ")[1].split(", ")
    min_x, max_x = x[2:].split("..")
    min_y, max_y = y[2:].split("..")
    return int(min_x), int(max_x), int(min_y), int(max_y)
