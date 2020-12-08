from re import search

input_file = open("input.txt", "r")

passports = input_file.read().split("\n\n")

print("Part 1")
valid_passports = 0
for passport in passports:
    if "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport and "hcl:" in passport and "ecl:" in passport \
            and "pid:" in passport:
        valid_passports += 1

print("Valid passports:", valid_passports)

print("Part 2")


def check_byr(passport: str) -> bool:
    result = search("byr:(\d\d\d\d)", passport)
    return result and 1920 <= int(result.group(1)) <= 2002


def check_iyr(passport: str) -> bool:
    result = search("iyr:(\d\d\d\d)", passport)
    return result and 2010 <= int(result.group(1)) <= 2020


def check_eyr(passport: str) -> bool:
    result = search("eyr:(\d\d\d\d)", passport)
    return result and 2020 <= int(result.group(1)) <= 2030


def check_hgt(passport: str) -> bool:
    result = search("hgt:(\d+)(cm|in)", passport)
    return result and (
            (result.group(2) == 'cm' and 150 <= int(result.group(1)) <= 193) or (result.group(2) == 'in' and 59 <= int(result.group(1)) <= 76))


def check_hcl(passport: str) -> bool:
    result = search("hcl:#([0-9a-f]+)", passport)
    return result and len(result.group(1)) == 6


def check_ecl(passport: str) -> bool:
    return search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) is not None


def check_pid(passport: str) -> bool:
    result = search("pid:([0-9]+)", passport)
    return result and len(result.group(1)) == 9


valid_passports = 0
for passport in passports:
    if check_byr(passport) and check_iyr(passport) and check_eyr(passport) and check_hgt(passport) and check_hcl(passport) and check_ecl(passport) \
            and check_pid(passport):
        valid_passports += 1

print("Valid passports:", valid_passports)
