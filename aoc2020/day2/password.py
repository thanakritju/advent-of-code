from typing import Sequence, Tuple


def password_check(password: str) -> bool:
    lower, upper, char_required, password = parse_input(password)

    count = 0
    for char in password:
        if char == char_required:
            count += 1

    return lower <= count <= upper


def password_check_v2(password: str) -> bool:
    lower, upper, char_required, password = parse_input(password)

    first_position = int(lower) - 1
    second_position = int(upper) - 1

    count = 0
    if (password[first_position] == char_required):
        count += 1
    if (password[second_position] == char_required):
        count += 1

    return count == 1


def count_valid_password(passwords: Sequence[str]) -> int:
    return sum([password_check(password) for password in passwords])


def count_valid_password_v2(passwords: Sequence[str]) -> int:
    return sum([password_check_v2(password) for password in passwords])


def parse_input(password: str) -> Tuple[int, int, str, str]:
    policy, password = password.split(":")
    number_range, char_required = policy.split(" ")
    password = password.strip()
    first_number, second_number = number_range.split("-")
    return int(first_number), int(second_number), char_required, password
