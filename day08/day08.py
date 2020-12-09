input_file = open("input.txt", "r")

instructions = input_file.read().splitlines()


def run(instruction_list: list) -> bool:
    accumulator = 0

    actual_position = 0
    visited_positions = set()

    while actual_position not in visited_positions and actual_position < len(instruction_list):
        visited_positions.add(actual_position)
        print(actual_position, instruction_list[actual_position], accumulator)
        (operation, argument) = instruction_list[actual_position].split(' ')
        if operation == 'acc':
            accumulator += int(argument)
            actual_position += 1
        elif operation == 'jmp':
            actual_position += int(argument)
        else:
            actual_position += 1

    print("Accumulator", accumulator)

    if actual_position >= len(instruction_list) - 1:
        print("Terminates")
        return True
    else:
        print("Infinite loop")
        return False


print("Part 1")
run(instructions)

print("Part 2")
instruction_index = 0
for instruction_index in range(0, len(instructions)):
    local_instructions = list(instructions)
    if 'jmp' in local_instructions[instruction_index]:
        local_instructions[instruction_index] = local_instructions[instruction_index].replace('jmp', 'nop')
    elif 'nop' in local_instructions[instruction_index]:
        local_instructions[instruction_index] = local_instructions[instruction_index].replace('nop', 'jmp')
    is_terminated = run(local_instructions)
    if is_terminated:
        break
