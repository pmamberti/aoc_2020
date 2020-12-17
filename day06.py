with open("day06_data", "r") as fin:
    group_answers = fin.read().split("\n\n")

# Part 1
answer_lines = [line.replace("\n", "") for line in group_answers]

score = 0

for line in answer_lines:
    score += len(set(line))

print(score)

# Part 2

answer_lines = [line.split("\n") for line in group_answers]
print(answer_lines[2])

total_everyone_score = 0

for line in answer_lines:
    max_occurrences = len(line)
    full_line = ("").join(line)
    everyone_answered_count = set()
    for letter in full_line:
        if full_line.count(letter) == max_occurrences:
            everyone_answered_count.add(letter)

    total_everyone_score += len(everyone_answered_count)

print(total_everyone_score)