input_file = open("input.txt", "r")

seat_ids = input_file.read().splitlines()

print("Part 1")


def set_bit(value: int, bit: int) -> int:
    return value | (1 << bit)


highest_seat_id = -1
numeric_seat_ids = []

for seat_id in seat_ids:
    row = 0
    for row_bit in range(7):
        if seat_id[row_bit] == 'B':
            row = set_bit(row, 6 - row_bit)
    column = 0
    for column_bit in range(7, 10):
        if seat_id[column_bit] == 'R':
            column = set_bit(column, 2 - column_bit + 7)
    numeric_seat_id = row * 8 + column
    print("{}: row {}, column {}, seta ID {}".format(seat_id, row, column, numeric_seat_id))
    numeric_seat_ids.append(numeric_seat_id)
    if numeric_seat_id > highest_seat_id:
        highest_seat_id = numeric_seat_id

print("Highest seat ID:", highest_seat_id)

print("Part 2")

for possible_id in range(highest_seat_id):
    if possible_id not in numeric_seat_ids and (possible_id + 1) in numeric_seat_ids and (possible_id - 1) in numeric_seat_ids:
        print("My seat id is", possible_id)
