expenses = []

with open("expenses", "r") as fin:
    for line in fin:
        expenses.append(int(line.strip()))

import itertools

e = itertools.combinations(expenses, 3)

for i in e:
    if i[0] + i[1] == 2020:
        print(i[0] * i[1])

for i in e:
    if (i[0]+i[1]+i[2] == 2020):
        print (i[0]*i[1]*i[2])