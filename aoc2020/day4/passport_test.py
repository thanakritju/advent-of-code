import pytest

from aoc2020.day4.passport import find_field, count_valid_passport, validate_field, count_valid_passport_with_validation


def test_count_valid_passport():
    test_input = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
        "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm",
        "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in",
    ]

    actual = count_valid_passport(test_input)

    assert actual == 2


def test_count_valid_passport_with_validation_invalid():
    test_input = [
        "eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946",
        "hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007",
    ]

    actual = count_valid_passport_with_validation(test_input)

    assert actual == 0


def test_count_valid_passport_with_validation_valid():
    test_input = [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f",
        "eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]

    actual = count_valid_passport_with_validation(test_input)

    assert actual == 4


@pytest.mark.parametrize(
    "test_field,expected",
    [
        ("hcl", "#ae17e1"),
        ("iyr", "2013"),
        ("eyr", "2024"),
        ("ecl", "brn"),
        ("pid", "760753108"),
        ("byr", "1931"),
        ("hgt", "179cm"),
        ("cid", None),
    ]
)
def test_find_field(test_field, expected):
    test_input = "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm"

    actual = find_field(test_field, test_input)

    assert actual == expected


@pytest.mark.parametrize(
    "test_field, field_value, expected",
    [
        ("byr", "2002", True),
        ("byr", "1920", True),
        ("byr", "1919", False),
        ("byr", "2003", False),
        ("eyr", "2020", True),
        ("eyr", "2030", True),
        ("eyr", "2019", False),
        ("eyr", "2031", False),
        ("iyr", "2010", True),
        ("iyr", "2020", True),
        ("iyr", "2009", False),
        ("iyr", "2021", False),
        ("hgt", "150cm", True),
        ("hgt", "140cm", False),
        ("hgt", "193cm", True),
        ("hgt", "194cm", False),
        ("hgt", "76in", True),
        ("hgt", "77in", False),
        ("hgt", "59in", True),
        ("hgt", "58in", False),
        ("hgt", "158m", False),
        ("hcl", "#123abc", True),
        ("hcl", "#123abz", False),
        ("hcl", "123abc", False),
        ("ecl", "brn", True),
        ("ecl", "wat", False),
        ("pid", "000000001", True),
        ("pid", "0123456789", False),
    ]
)
def test_validate_field(test_field, field_value, expected):
    actual = validate_field(test_field, field_value)

    assert actual == expected


@pytest.mark.puzzle
def test_count_valid_passport_for_puzzle_input():
    puzzle_input = open("aoc2020/day4/passports.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_valid_passport(content)

    assert actual == 228


@pytest.mark.puzzle
def test_count_valid_passport_with_validation_for_puzzle_input():
    puzzle_input = open("aoc2020/day4/passports.txt", "r")
    content = puzzle_input.read().split("\n\n")

    actual = count_valid_passport_with_validation(content)

    assert actual == 175
