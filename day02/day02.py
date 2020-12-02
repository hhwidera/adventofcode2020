import re

input_file = open("input.txt", "r")

lines = input_file.read().splitlines()

print("Part 1")
valid_password_counter = 0
for line in lines:
    (policy_part, password) = line.split(': ')
    (lowest_highest_number_times_part, letter) = policy_part.split(' ')
    lowest_number_part = int(lowest_highest_number_times_part.split('-')[0])
    highest_number_part = int(lowest_highest_number_times_part.split('-')[1])
    count_of_letters_in_password = len(re.findall(letter, password))
    if lowest_number_part <= count_of_letters_in_password <= highest_number_part:
        valid_password_counter += 1
print("Counter of valid passwords:", valid_password_counter)

print("Part 2")
valid_password_counter = 0
for line in lines:
    (policy_part, password) = line.split(': ')
    (first_second_position_part, letter) = policy_part.split(' ')
    first_position = int(first_second_position_part.split('-')[0])
    second_position = int(first_second_position_part.split('-')[1])
    if (password[first_position - 1] == letter) != (password[second_position - 1] == letter):
        valid_password_counter += 1
print("Counter of valid passwords:", valid_password_counter)