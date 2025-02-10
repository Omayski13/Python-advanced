n = int(input())
car_number = input()
matrix= []
car_row,car_col = 0,0
tunel_1_row, tunel_1_col = None, None
tunel_2_row, tunel_2_col = None, None
tunel_count = 0
for row_index in range(n):
    col_input = list(input().split())
    matrix.append(col_input)
    for el in col_input:
        if el == "T":
            if tunel_count == 0:
                tunel_1_row,tunel_1_col = row_index, col_input.index("T")
                tunel_count += 1
            else:
                tunel_2_row, tunel_2_col = row_index, col_input.index("T")

kilometers = 0
while True:
    command = input()
    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break
    next_row, next_col = None, None
    if command == "left":
        next_row, next_col = car_row, car_col - 1
    if command == "right":
        next_row, next_col = car_row, car_col + 1
    if command == "up":
        next_row, next_col = car_row -1, car_col
    if command == "down":
        next_row, next_col = car_row +1, car_col

    if matrix[next_row][next_col] == ".":
        kilometers += 10
        car_row, car_col = next_row, next_col
    if matrix[next_row][next_col] == "T":
        kilometers += 30
        matrix[next_row][next_col] = "."
        if next_row == tunel_1_row and next_col == tunel_1_col:
            car_row, car_col = tunel_2_row, tunel_2_col
        elif next_row == tunel_2_row and next_col == tunel_2_col:
            car_row, car_col = tunel_1_row, tunel_1_col
        matrix[car_row][car_col] = "."
    if matrix[next_row][next_col] == "F":
        print(f"Racing car {car_number} finished the stage!")
        kilometers += 10
        car_row, car_col = next_row, next_col
        break
matrix[car_row][car_col] = "C"
print(f"Distance covered {kilometers} km.")
for row in matrix:
    print("".join(row))



