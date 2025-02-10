
def next_move(command,current_row,current_col,rows,cols):
    if command == "right":
        if current_col + 1 > cols -1:
            return current_row,0
        else:
            return current_row,current_col+1
    if command == "left":
        if current_col - 1 < 0:
            return current_row, cols - 1
        else:
            return current_row,current_col - 1
    if command == "down":
        if current_row + 1 > rows -1:
            return 0,current_col
        else:
            return current_row + 1,current_col
    if command == "up":
        if current_row - 1 < 0:
            return rows -1 ,current_col
        else:
            return current_row - 1,current_col

rows, cols = [int(x) for x in input().split(", ")]
current_row, current_col = None, None
matrix = []
sum_to_collect = 0
decorations = 0
cookies = 0
gifts = 0
christmas = False
for row_index in range(rows):
    col_input = list(input().split())
    matrix.append(col_input)
    for el in col_input:
        if el == "Y":
            current_row, current_col = row_index, col_input.index("Y")
        elif el == "D" or el == "C" or el == "G":
            sum_to_collect += 1
command = input()

while command != "End":

    split_command = command.split("-")
    current_command = split_command[0]
    steps = int(split_command[1])
    for step in range(1 , steps+1):
        if sum_to_collect == cookies + gifts + decorations:
            christmas = True
            break

        matrix[current_row][current_col] = "x"
        next_row,next_col = next_move(current_command,current_row,current_col,rows,cols)
        if matrix[next_row][next_col] == "D":
            decorations += 1
            current_row,current_col = next_row,next_col
            continue
        if matrix[next_row][next_col] == "C":
            cookies += 1
            current_row,current_col = next_row,next_col
            continue
        if matrix[next_row][next_col] == "G":
            gifts += 1
            current_row,current_col = next_row,next_col
            continue
        current_row, current_col = next_row, next_col
    if christmas:
        print("Merry Christmas!")
        break

    command = input()

matrix[current_row][current_col] = "Y"
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for row in matrix:
    print(*row)




