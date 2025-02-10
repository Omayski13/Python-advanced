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
    if command == 'right' and not is_valid(current_col + 1, cols):
        return current_row, None

matrix= []
rows = int(input())
cols = rows
sinked = False

boat_row,boat_col = None,None

for row_index in range(rows):
    col_input = list(input())
    matrix.append(col_input)
    if "S" in col_input:
        for el in col_input:
            boat_row, boat_col = row_index,col_input.index("S")

fish_tons = 0

while True:
    command = input()
    if command == "collect the nets":
        break
    matrix[boat_row][boat_col] = "-"

    next_row,next_col = next_move(command,boat_row,boat_col)

    if command == "right" and next_col == None:
        next_col = 0
    if command == "left" and next_col == None:
        next_col = cols - 1
    if command == "up" and next_row == None:
        next_row = rows - 1
    if command == "down" and next_row == None:
        next_row = 0


    if matrix[next_row][next_col] == "W":
        fish_tons = 0
        sinked = True
        boat_row,boat_col = next_row,next_col
        break
    if matrix[next_row][next_col] == "-":
        boat_row, boat_col = next_row, next_col
        continue
    else:
        fish_tons += int(matrix[next_row][next_col])
        boat_row, boat_col = next_row, next_col
        matrix[boat_row][boat_col] = "-"
matrix[boat_row][boat_col] = "S"
if sinked:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{boat_row},{boat_col}]")
else:
    if fish_tons >= 20:
        print("Success! You managed to reach the quota!")
        print(f"Amount of fish caught: {fish_tons} tons.")
        for row in matrix:
            print("".join(row))
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_tons} tons of fish more.")
        if fish_tons > 0:
            print(f"Amount of fish caught: {fish_tons} tons.")
        for row in matrix:
            print("".join(row))

