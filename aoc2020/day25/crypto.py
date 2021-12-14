def hack(card_pub, door_pub):
    card_loop_size = None
    door_loop_size = None
    number = 1
    loop_size = 1
    while card_loop_size is None and door_loop_size is None:
        number = number * 7 % 20201227

        if number == card_pub:
            return loop(door_pub, loop_size)

        if number == door_pub:
            return loop(card_pub, loop_size)

        loop_size += 1


def loop(subject_number, loop_size):
    answer = 1
    for _ in range(loop_size):
        answer = answer * subject_number % 20201227
    return answer
