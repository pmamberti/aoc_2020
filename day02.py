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


def check_password_new_policy(password, char, pos_1, pos_2):
    if (char == password[pos_1 - 1] and char != password[pos_2 - 1]) or (
        char != password[pos_1 - 1] and char == password[pos_2 - 1]
    ):
        return True
    else:
        return False


if __name__ == "__main__":

    passwords_list = []

    with open("day02_data", "r") as fin:
        valid_count_old = 0
        valid_count_new = 0

        for line in fin:
            passwords_list.append(line)
            raw_data = clean_data(line)
            requirements_char = raw_data[1].strip(":")
            requirements_min = int(raw_data[0].split("-")[0])
            requirements_max = int(raw_data[0].split("-")[1])
            pw_string = raw_data[2]

            old_policy_check = check_password(
                password=pw_string,
                char=requirements_char,
                max=requirements_max,
                min=requirements_min,
            )

            if old_policy_check:
                valid_count_old += 1

            new_policy_check = check_password_new_policy(
                password=pw_string,
                char=requirements_char,
                pos_1=requirements_min,
                pos_2=requirements_max,
            )

            if new_policy_check:
                valid_count_new += 1

        print(f"Old Policy Count of valid passwords: {valid_count_old}")
        print(f"New Policy Count of valid passwords: {valid_count_new}")