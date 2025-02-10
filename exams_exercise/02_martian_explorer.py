from collections import deque

def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'up' and not is_valid(current_row-1, rows):
        return None,current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'down' and not is_valid(current_row+1, rows):
        return None, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'left' and not is_valid(current_col-1, cols):
        return current_row, None
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    if command == 'right' and is_valid(current_col + 1, cols):
        return current_row, None



rows, cols = 6, 6
matrix = []
rover_row, rover_col = None, None
for row_index in range(rows):
    col_input = list(input().split())
    matrix.append(col_input)
    for el in col_input:
        if el == "E":
            rover_row, rover_col = row_index, col_input.index("E")

commands = input().split(", ")
water = 0
metal = 0
concrete = 0
broken_rover = False
while commands:
    command = commands[0]
    commands.remove(command)
    next_row, next_col = next_move(command,rover_row,rover_col)
    if next_row is None or next_col is None:
        if command == "down":
            next_row = 0
        elif command == "up":
            next_row = 5
    if next_col is None:
        if command == "right":
            next_col = 0
        elif command == "left":
            next_col = 5
    if matrix[next_row][next_col] == "-":
        rover_row, rover_col = next_row, next_col
        continue
    if matrix[next_row][next_col] == "W":
        print(f"Water deposit found at ({next_row}, {next_col})")
        water += 1
        rover_row, rover_col = next_row, next_col
        matrix[rover_row][rover_col] = "-"
        continue
    if matrix[next_row][next_col] == "M":
        print(f"Metal deposit found at ({next_row}, {next_col})")
        metal += 1
        rover_row, rover_col = next_row, next_col
        matrix[rover_row][rover_col] = "-"
        continue
    if matrix[next_row][next_col] == "C":
        print(f"Concrete deposit found at ({next_row}, {next_col})")
        concrete += 1
        rover_row, rover_col = next_row, next_col
        matrix[rover_row][rover_col] = "-"
        continue
    if matrix[next_row][next_col] == "R":
        rover_row, rover_col = next_row, next_col
        broken_rover = True
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
if metal > 0 and water > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


