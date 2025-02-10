def next_move(command,row,col):
    if command == "up":
        return row - 1, col
    if command == "down":
        return row + 1, col
    if command == "left":
        return row , col - 1
    if command == "right":
        return row , col + 1

matrix = []
rows = int(input())
car_number = input()
cols = rows
t1_row,t1_col = None, None
t2_row,t2_col = None, None
car_row,car_col = 0,0
kilometers = 0
finished = False
counter = 0
for row_index in range(rows):
    col_input = input().split()
    matrix.append(col_input)
    if "T" in col_input:
        if counter == 0:
            t1_row,t1_col = row_index,col_input.index("T")
            counter+=1
        else:
            t2_row,t2_col = row_index,col_input.index("T")

while True:
    command = input()
    if command == "End":
        break
    next_row,next_col = next_move(command,car_row,car_col)
    if matrix[next_row][next_col] == ".":
        car_row,car_col = next_row,next_col
        kilometers += 10
        continue
    if matrix[next_row][next_col] == "T":
        kilometers += 30
        matrix[next_row][next_col] = "."
        if next_row == t1_row and next_col == t1_col :
            car_row,car_col = t2_row,t2_col
        if next_row == t2_row and next_col == t2_col:
            car_row,car_col = t1_row,t1_col
        matrix[car_row][car_col] = "."
        continue

    if matrix[next_row][next_col] == "F":
        finished = True
        kilometers += 10
        car_row,car_col = next_row,next_col
        print(f"Racing car {car_number} finished the stage!")
        break

if not finished:
    print(f"Racing car {car_number} DNF.")
print(f"Distance covered {kilometers} km.")
matrix[car_row][car_col] = "C"
for row in matrix:
    print("".join(row))



