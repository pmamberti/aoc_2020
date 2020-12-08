with open("day03_data", "r") as fin:
    woods_map = fin.readlines()

# Create the map we need to not parse the \n cause I have no idea how to do that
with open("day03_full_map", "w") as fout:
    needed_steps = len(woods_map)
    needed_columns = round(needed_steps / len(woods_map[0])) + 1
    new_lines = [(line.strip() * needed_columns * 3) + "\n" for line in woods_map]
    fout.writelines(new_lines)

x = 0
y = 0
tree_count = 0

with open("day03_full_map", "r") as fin:
    full_map = fin.readlines()
    print(len(full_map))
    while y < len(full_map):
        position = full_map[y][x]
        print(y, len(position), position)
        if position == "#":
            tree_count += 1

        x += 3
        y += 1

print(tree_count)