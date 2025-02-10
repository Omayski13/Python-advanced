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

rows,cols = [int(x) for x in input().split()]
matrix = []
start_row,start_col = None,None
boy_row, boy_col = None,None
late = False
command = ' '

for row_index in range(rows):
    row_input = list(input())
    for el in row_input:
        if el == "B":
            boy_row, boy_col = row_index, row_input.index("B")
            start_row, start_col = row_index, row_input.index("B")
    matrix.append(row_input)

while command:
    command = input()
    next_row,next_col = next_move(command,boy_row,boy_col)
    if next_row is None or next_col is None:
        print("The delivery is late. Order is canceled.")
        matrix[start_row][start_col] = " "
        break
    if matrix[next_row][next_col] == "*":
        continue
    if matrix[next_row][next_col] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[boy_row][boy_col] = "."
        boy_row, boy_col = next_row, next_col
        matrix[boy_row][boy_col] = "R"
        continue
    if matrix[next_row][next_col] == "A":
        matrix[boy_row][boy_col] = "."
        boy_row,boy_col = next_row,next_col
        matrix[boy_row][boy_col] = "P"
        matrix[start_row][start_col] = 'B'
        print("Pizza is delivered on time! Next order...")
        break
    if not matrix[boy_row][boy_col] == 'R':
        matrix[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    matrix[boy_row][boy_col] = '.'
    continue

for row in matrix:
    print("".join(row))


