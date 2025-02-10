from collections import deque

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
commands = deque(input().split(", "))
squirell_row,squirell_col = None,None
hazelnuts = 3

for row_index in range(rows):
    col_input = list(input())
    for el in col_input:
        if el == "s":
            squirell_row,squirell_col = row_index,col_input.index("s")
    matrix.append(col_input)
while True:
    if hazelnuts == 0:
        print("Good job! You have collected all hazelnuts!")
        break
    if not commands:
        print("There are more hazelnuts to collect.")
        break
    command = commands.popleft()
    next_row,next_col = next_move(command,squirell_row,squirell_col)
    if next_row is None or next_col is None:
        print("The squirrel is out of the field.")
        break
    if matrix[next_row][next_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if matrix[next_row][next_col] == "h":
        hazelnuts -= 1
        squirell_row,squirell_col = next_row,next_col
        matrix[squirell_row][squirell_col] = "*"
        continue
    if matrix[next_row][next_col] == "*":
        squirell_row, squirell_col = next_row, next_col

print(f"Hazelnuts collected: {3 - hazelnuts}")
