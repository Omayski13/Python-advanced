def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None
rows = int(input())
cols = rows
matrix = []
sub_row, sub_col = None, None
for row_index in range(rows):
    col_input = list(input())
    matrix.append(col_input)
    for el in col_input:
        if el == "S":
            sub_row, sub_col = row_index, col_input.index("S")

damages = 0
destroyed = 0

while True:
    command = input()
    if damages == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_row}, {sub_col}]!")
        break
    if destroyed == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    next_row,next_col = next_move(command,sub_row,sub_col)
    if matrix[next_row][next_col] == "-":
        matrix[sub_row][sub_col] = "-"
        sub_row,sub_col = next_row,next_col
        matrix[sub_row][sub_col] = "S"
        continue
    if matrix[next_row][next_col] == "*":
        damages += 1
        matrix[sub_row][sub_col] = "-"
        sub_row,sub_col = next_row,next_col
        matrix[sub_row][sub_col] = "S"
        continue
    if matrix[next_row][next_col] == "C":
        destroyed += 1
        matrix[sub_row][sub_col] = "-"
        sub_row,sub_col = next_row,next_col
        matrix[sub_row][sub_col] = "S"

for row in matrix:
    print("".join(row))



