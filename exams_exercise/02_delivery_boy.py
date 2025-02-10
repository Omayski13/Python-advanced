def position_valid(row,coll,row_size,col_size):
    return 0 <= row < row_size and 0 <= coll < col_size

ROW_SIZE,COLL_SIZE = [int(x) for x in input().split()]
matrix = []
starting_row,starting_col = 0,0
restaurant_row,restaurant_coll = 0,0
adress_row,adress_coll = 0,0
boy_row,boy_coll = 0,0

late_delivery = False

for row_index in range(ROW_SIZE):
    row_input = list(input())
    for el in row_input:
        if el == "B":
            starting_row,starting_col =row_index,row_input.index("B")
            boy_row,boy_coll =row_index,row_input.index("B")
        if el == "A":
            adress_row,adress_coll = row_index,row_input.index("A")
        if el == "P":
            restaurant_row,restaurant_coll = row_index,row_input.index("P")
    matrix.append(row_input)


while matrix[adress_row][adress_coll] != "P":
    command = input()
    if command == "left":
        if position_valid(boy_row, boy_coll - 1, ROW_SIZE, COLL_SIZE):
            if matrix[boy_row][boy_coll - 1] == "*":
                continue
            if matrix[boy_row][boy_coll - 1] == "-":
                matrix[boy_row][boy_coll] = "."
            if matrix[boy_row][boy_coll - 1] == "P":
                print("Pizza is collected. 10 minutes for delivery.")
                matrix[boy_row][boy_coll - 1] = "R"
            if matrix[boy_row][boy_coll - 1] == "A":
                print("Pizza is delivered on time! Next order...")
                matrix[boy_row][boy_coll - 1] = "P"
                break
            boy_coll -= 1
        else:
            print("The delivery is late. Order is canceled.")
            late_delivery =True
            break
    if command == "right":
        if position_valid(boy_row, boy_coll + 1, ROW_SIZE, COLL_SIZE):
            if matrix[boy_row][boy_coll + 1] == "*":
                continue
            if matrix[boy_row][boy_coll + 1 ] == "-":
                matrix[boy_row][boy_coll] = "."
            if matrix[boy_row][boy_coll + 1] == "P":
                print("Pizza is collected. 10 minutes for delivery.")
                matrix[boy_row][boy_coll + 1] = "R"
                matrix[boy_row][boy_coll] = "."
            if matrix[boy_row][boy_coll+1] == "A":
                print("Pizza is delivered on time! Next order...")
                matrix[boy_row][boy_coll+1] = "P"
                break
            boy_coll += 1
        else:
            print("The delivery is late. Order is canceled.")
            late_delivery = True
            break
    if command == "down":
        if position_valid(boy_row + 1, boy_coll, ROW_SIZE, COLL_SIZE):
            if matrix[boy_row + 1][boy_coll] == "*":
                continue
            if matrix[boy_row +1 ][boy_coll] == "-":
                matrix[boy_row][boy_coll] = "."
            if matrix[boy_row+1][boy_coll] == "P":
                print("Pizza is collected. 10 minutes for delivery.")
                matrix[boy_row+1][boy_coll] = "R"
            if matrix[boy_row+1][boy_coll] == "A":
                print("Pizza is delivered on time! Next order...")
                matrix[boy_row+1][boy_coll] = "P"
                break
            boy_row += 1
        else:
            print("The delivery is late. Order is canceled.")
            late_delivery = True
            break
    if command == "up":
        if position_valid(boy_row - 1, boy_coll - 1, ROW_SIZE, COLL_SIZE):
            if matrix[boy_row - 1][boy_coll] == "*":
                continue
            if matrix[boy_row - 1 ][boy_coll] == "-":
                matrix[boy_row][boy_coll] = "."
            if matrix[boy_row - 1][boy_coll] == "P":
                print("Pizza is collected. 10 minutes for delivery.")
                matrix[boy_row - 1][boy_coll] = "R"
            if matrix[boy_row-1][boy_coll] == "A":
                print("Pizza is delivered on time! Next order...")
                matrix[boy_row][boy_coll] ="."
                matrix[boy_row-1][boy_coll] = "P"
                break
            boy_row -= 1
        else:
           print("The delivery is late. Order is canceled.")
           late_delivery = True
           break

if late_delivery:
    matrix[starting_row][starting_col] = " "
else:
    matrix[starting_row][starting_col] = "B"
    matrix[restaurant_row][restaurant_coll] = "R"

for row in matrix:
    print("".join(row))

