from typing import Sequence
import re


required_fields = {
    "byr": r"19[2-9][0-9]|200[0-2]",
    "iyr": r"2010|2020|201[0-9]",
    "eyr": r"2020|2030|202[0-9]",
    "hgt": r"1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in",
    "hcl": r"#[0-9a-f]{6}",
    "ecl": r"amb|blu|brn|gry|grn|hzl|oth",
    "pid": r"[0-9]{9}",
}


def count_valid_passport(passports: Sequence[str]) -> int:
    count = 0
    for passport in passports:
        if all([find_field(field, passport) for field in required_fields.keys()]):
            count += 1
    return count


def count_valid_passport_with_validation(passports: Sequence[str]) -> int:
    count = 0
    for passport in passports:
        if all([find_and_validate_field(field, passport) for field in required_fields.keys()]):
            count += 1
    return count


def find_field(field_name: str, passport: str) -> str:
    m = re.search(rf"{field_name}:([^\s]+)", passport)
    return m.group(1) if m else None


def find_and_validate_field(field_name: str, passport: str) -> bool:
    field_value = find_field(field_name, passport)
    return validate_field(field_name, field_value) if field_value else False


def validate_field(field_name: str, field_value: str) -> bool:
    m = re.search(rf"^({required_fields[field_name]})$", field_value)
    return bool(m)
