import re

with open("day04_data", "r", newline="\n") as fin:
    all_passports = fin.readlines()

ordered_passports = []
buffer = []

for line in all_passports:
    splitline = line.split()
    # print(splitline)
    if splitline:
        buffer.extend(splitline)
        print(buffer)
    else:
        ordered_passports.append(buffer)
        buffer = []
        continue

valid_count = 0
required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

for passport in ordered_passports:
    existing_fields = [field.split(":")[0] for field in passport]
    if all(field in existing_fields for field in required_fields):
        valid_count += 1

print(valid_count)