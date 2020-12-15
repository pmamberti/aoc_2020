import re

with open("day04_data", "r", newline="\n") as fin:
    all_passports = fin.readlines()

clean_passports = []
buffer = []

for line in all_passports:
    splitline = line.split()
    # print(splitline)
    if splitline:
        buffer.extend(splitline)
        # print(buffer)
    else:
        clean_passports.append(buffer)
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

# Problem #1

valid_passports = []

for passport in clean_passports:
    joint_passport = " ".join(passport)
    split_passport = re.split(" |:", joint_passport)
    passport_fields = split_passport[::2]
    fields_values = split_passport[1::2]
    print(passport_fields, fields_values)

    if all(field in passport_fields for field in required_fields):
        valid_count += 1
        passport_dict = dict(zip(passport_fields, fields_values))
        valid_passports.append(passport_dict)

print(valid_count)

# Problem #2
def check_strict_requirements(passport=dict):
    birth_year = passport.get("byr", "n/a")
    issue_year = passport.get("iyr", "n/a")
    expiration_year = passport.get("eyr", "n/a")
    height = passport.get("hgt", "n/a")
    hair_color = passport.get("hcl", "n/a")
    eye_color = passport.get("ecl", "n/a")
    passport_id = passport.get("pid", "n/a")

    hair_check = re.compile("#[0-9|a-f]{6,6}")
    eye_check = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid_check = re.compile("[0-9]{9,9}")

    if (
        len(birth_year) == 4
        and 1920 <= int(birth_year) <= 2002
        and (len(issue_year) == 4 and 2010 <= int(issue_year) <= 2020)
        and (len(expiration_year) == 4 and 2020 <= int(expiration_year) <= 2030)
        and (
            (height[-2:] == "cm" and 150 <= int(height[:-2]) <= 193)
            or (height[-2:] == "in" and 59 <= int(height[:-2]) <= 76)
        )
        and (len(hair_color) == 7 and hair_check.match(hair_color))
        and (eye_color in eye_check)
        and (len(passport_id) == 9 and pid_check.match(passport_id))
    ):
        return True
    else:
        return False


really_valid_passports = 0

for passport in valid_passports:
    if check_strict_requirements(passport):
        really_valid_passports += 1

print(f"Really Valid Passports: {really_valid_passports}/{valid_count}")