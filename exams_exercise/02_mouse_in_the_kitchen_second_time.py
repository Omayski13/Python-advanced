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

rows,cols = [int(x) for x in input().split(",")]

mouse_row,mouse_col = 0,0
cheeses = 0
matrix = []
for row_index in range(rows):
    col_input = list(input())
    cheeses += col_input.count("C")
    for el in col_input:
        if el == "M":
            mouse_row,mouse_col=row_index,col_input.index("M")
    matrix.append(col_input)
command = input()
while cheeses != 0:
    if command == "danger":
        print("Mouse will come back later!")
        break
    next_row,next_col = next_move(command,mouse_row,mouse_col)
    if next_row is None or next_col is None:
        print("No more cheese for tonight!")
        break
    if matrix[next_row][next_col] == "@":
        command = input()
        continue
    if matrix[next_row][next_col] == "C":
        cheeses -= 1
        matrix[mouse_row][mouse_col] = "*"
        mouse_row,mouse_col = next_row,next_col
        matrix[mouse_row][mouse_col] = "M"
        command = input()
        continue
    if matrix[next_row][next_col] == "T":
        matrix[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = "M"
        print("Mouse is trapped!")
        break
    if matrix[next_row][next_col] == "*":
        matrix[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = "M"
        command = input()
        continue

    command = input()
else:
    print("Happy mouse! All the cheese is eaten, good night!")

for row in matrix:
    print(''.join(row))


