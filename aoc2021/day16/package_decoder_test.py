import pytest

from aoc2021.day16.package_decoder import decode, sum_of_version_numbers, value


@pytest.mark.parametrize(
    "encoded,expected",
    [
        ("D2FE28", (6, 4, 2021, None, 0)),
        ("38006F45291200", (1, 6, None, "0", 2)),
        ("EE00D40C823060", (7, 3, None, "1", 3)),
    ]
)
def test_decode(encoded, expected):
    actual = decode(encoded)

    assert actual == expected


@pytest.mark.parametrize(
    "encoded,expected",
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ]
)
def test_sum_of_version_numbers(encoded, expected):
    actual = sum_of_version_numbers(encoded)

    assert actual == expected


@pytest.mark.puzzle
def test_sum_of_version_numbers_for_puzzle():
    puzzle_input = open("aoc2021/day16/input.txt", "r")
    content = puzzle_input.read()

    actual = sum_of_version_numbers(content)

    assert actual == 986


@pytest.mark.parametrize(
    "encoded,expected",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ]
)
def test_value(encoded, expected):
    actual = value(encoded)

    assert actual == expected


@pytest.mark.puzzle
def test_sum_of_version_numbers_for_puzzle():
    puzzle_input = open("aoc2021/day16/input.txt", "r")
    content = puzzle_input.read()

    actual = value(content)

    assert actual == 18234816469452
