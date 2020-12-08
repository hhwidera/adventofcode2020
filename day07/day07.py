input_file = open("input.txt", "r")

rules_input = input_file.read().splitlines()

rules = {}

for role_input in rules_input:
    (bag, bag_contain) = role_input.split(' bags contain ')
    if 'no other bags' in bag_contain:
        rules[bag] = {}
    else:
        contains = bag_contain.split(', ')
        contain_list = list()
        for contain in contains:
            contain_parts = contain.split(' ')
            count = int(contain_parts[0])
            color = contain_parts[1] + ' ' + contain_parts[2]
            contain_list.append((color, count))
        rules[bag] = set(contain_list)
print(rules)

print("Part 1")


def is_color_contains(actual_color: str, search_color: str) -> bool:
    sub_bags = rules[actual_color]
    for sub_bag in sub_bags:
        if sub_bag[0] == search_color:
            return True
        if is_color_contains(sub_bag[0], search_color):
            return True
    return False


number_of_contains = 0
for color in rules.keys():
    is_contain_shiny_gold = is_color_contains(color, 'shiny gold')
    print(color, ":", is_contain_shiny_gold)
    if is_contain_shiny_gold:
        number_of_contains += 1
print("Contains", number_of_contains)

print("Part 2")


def number_of_bags_inside(actual_color: str) -> int:
    sub_bags = rules[actual_color]
    bags = 1
    for sub_bag in sub_bags:
        bags += number_of_bags_inside(sub_bag[0]) * sub_bag[1]
    return bags


print("Bags inside shiny gold:", number_of_bags_inside('shiny gold') - 1)
