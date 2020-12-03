
input_file = open("input.txt", "r")

lines = input_file.read().splitlines()

print("Part 1")
tree_encounter = 0
position_x = 0
for line in lines[1:]:
    position_x = (position_x + 3) % len(line)
    if line[position_x] == '#':
        tree_encounter += 1
print("Tree encounter:", tree_encounter)


print("Part 2")


def tree_going(steps_right: int, steps_down: int) -> int:
    tree_encounter = 0
    position_x = 0
    for position_y in range(steps_down, len(lines), steps_down):
        line = lines[position_y]
        position_x = (position_x + steps_right) % len(line)
        if line[position_x] == '#':
            tree_encounter += 1
    print("Tree encounter for right {} and down {}: {}".format(steps_right, steps_down, tree_encounter))
    return tree_encounter


print("Multiply:",  tree_going(1, 1) *
                    tree_going(3, 1) *
                    tree_going(5, 1) *
                    tree_going(7, 1) *
                    tree_going(1, 2))
