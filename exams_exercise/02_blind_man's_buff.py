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
buf_row,buf_col = None,None
touched_people = 0
moves = 0

for row_index in range(rows):
    col_input = list(input().split())
    matrix.append(col_input)
    for el in col_input:
        if el == "B":
            buf_row, buf_col = row_index,col_input.index("B")

start_col,start_row = buf_row,buf_col

while True:
    if moves == 1:
       matrix[start_row][start_col] = "-"
    command = input()
    if command == "Finish" or touched_people == 3:
        break
    next_row,next_col = next_move(command,buf_row,buf_col)
    if next_row is None or next_col is None:
        continue
    if matrix[next_row][next_col] == "O":
        continue
    if matrix[next_row][next_col] == "P":
        touched_people += 1
        moves += 1
        buf_row,buf_col=next_row,next_col
        matrix[buf_row][buf_col] = "-"
        continue
    if matrix[next_row][next_col] == "-":
        moves += 1
        buf_row, buf_col = next_row, next_col

print("Game over!")
print(f"Touched opponents: {touched_people} Moves made: {moves}")



