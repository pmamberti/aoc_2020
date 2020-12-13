import re

with open("day04_data", "r", newline="\n") as fin:
    all_passports = fin.readlines()

content = []
buffer = []

for line in all_passports:
    if line != "\n":
        buffer.append(line.strip("\n"))
        print(type(buffer))
    else:
        content += buffer
        buffer = ""

for c in content:
    c = re.split(":| ", c)
    c.pop(0)
    # print(c)


required = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

valid_count = 0

for c in content:
    # result = all(list(c) for req_field in required)
    print(list(c))
    # if result:
    #     valid_count += 1

print(len(content))
print(valid_count)