def clean_data(string):
    split_line = string.split(" ")
    return split_line


def check_password(password, char, min=0, max=0):
    """Checks if the password is valid according to requirements"""
    letter_count = 0
    for letter in password:
        if letter == char:
            letter_count += 1

    if letter_count in range(min, max + 1):
        return True
    else:
        return False


if __name__ == "__main__":

    passwords_list = []

    with open("day02_data", "r") as fin:
        valid_count = 0

        for line in fin:
            passwords_list.append(line)
            raw_data = clean_data(line)
            requirements_char = raw_data[1].strip(":")
            requirements_min = int(raw_data[0].split("-")[0])
            requirements_max = int(raw_data[0].split("-")[1])
            pw_string = raw_data[2]
            if check_password(
                password=pw_string,
                char=requirements_char,
                max=requirements_max,
                min=requirements_min,
            ):
                valid_count += 1

        print(valid_count)