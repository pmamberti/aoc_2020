def create_map(x_increment):
    with open("day03_data", "r") as fin:
        woods_map = fin.readlines()

    # Create the map we need to not parse the \n cause I have no idea how to do that
    with open("day03_full_map", "w") as fout:
        needed_steps = len(woods_map)
        needed_columns = round(needed_steps / len(woods_map[0])) + 1
        new_lines = [
            (line.strip() * needed_columns * x_increment) + "\n" for line in woods_map
        ]
        fout.writelines(new_lines)


def count_trees(increment_x, increment_y):
    x = 0
    y = 0
    tree_count = 0

    with open("day03_full_map", "r") as fin:
        full_map = fin.readlines()
        while y < len(full_map):
            position = full_map[y][x]
            if position == "#":
                tree_count += 1

            x += increment_x
            y += increment_y

    return tree_count


if __name__ == "__main__":
    slopes = [
        {"increment_x": 1, "increment_y": 1},
        {"increment_x": 3, "increment_y": 1},
        {"increment_x": 5, "increment_y": 1},
        {"increment_x": 7, "increment_y": 1},
        {"increment_x": 1, "increment_y": 2},
    ]

    total_trees = 1

    for slope in slopes:
        create_map(x_increment=slope.get("increment_x"))
        slope_count = count_trees(slope.get("increment_x"), slope.get("increment_y"))
        total_trees *= slope_count

    print(total_trees)