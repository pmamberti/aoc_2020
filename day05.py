# https://adventofcode.com/2020/day/5

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.


def get_row(pid):
    low = 0
    high = 128
    row_str = pid[:7]

    for l in row_str:

        pos = [x for x in range(low, high)]
        increment = len(pos)

        if l == "B":
            low += int(increment / 2)
        else:
            high -= int(increment / 2)

        if increment == 2:
            if l == "B":
                row = pos[1]
            else:
                row = pos[0]
    return row


def get_column(pid):
    seat_low = 0
    seat_high = 8
    column = pid[7:]

    for l in column:

        pos = [x for x in range(seat_low, seat_high)]
        increment = len(pos)

        if l == "R":
            seat_low += int(increment / 2)
        else:
            seat_high -= int(increment / 2)
            (increment / 2)

        if increment == 2:
            if l == "L":
                column = pos[0]
            else:
                column = pos[1]

    return column


with open("day05_data", "r") as fin:
    all_pass_ids = fin.readlines()

all_seat_ids = []

for passport_id in all_pass_ids:
    row = get_row(passport_id)
    column = get_column(passport_id)

    seat_id = row * 8 + column
    all_seat_ids.append(seat_id)

all_seat_ids = sorted(all_seat_ids)
print(all_seat_ids[-1])

i = 0
start = all_seat_ids[0]
end = all_seat_ids[-1]
my_seat = set(range(start, end + 1)).difference(all_seat_ids)
print(my_seat)
