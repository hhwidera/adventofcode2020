
input_file = open("input.txt", "r")

numbers = [int(numeric_string) for numeric_string in input_file.read().splitlines()]

print("Part 1")
for number_index in range(len(numbers) - 1):
    for other_index in range(number_index - 1):
        if numbers[number_index] + numbers[other_index] == 2020:
            print("Found", numbers[number_index], "and", numbers[other_index], ". Multiplying:", numbers[number_index] * numbers[other_index])

print("Part 2")
for number_index in range(len(numbers) - 1):
    for other_index in range(number_index - 1):
        for other_other_index in range(other_index - 1):
            if numbers[number_index] + numbers[other_index] + numbers[other_other_index] == 2020:
                print("Found", numbers[number_index], ",", numbers[other_index], "and", numbers[other_other_index], ". Multiplying:",
                      numbers[number_index] * numbers[other_index] * numbers[other_other_index])
