def position_valid(row,coll,N,M):
    return 0 <= row < N and 0 <= coll < M



N,M = [int(x) for x in input().split(",")]

matrix = []
mouse_row,mouse_coll = 0,0
total_cheeses = 0

for row_index in range(N):
    collum_input = list(input())
    total_cheeses += collum_input.count("C")
    matrix.append(collum_input)
    for el in collum_input:
        if el == "M":
            mouse_row,mouse_coll = row_index, collum_input.index("M")


command = input()
while command != "danger":
    if total_cheeses == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        break
    if command == "left":
        if position_valid(mouse_row,mouse_coll-1,N,M):
            if matrix[mouse_row][mouse_coll-1] == "@":
                command = input()
                continue
            elif matrix[mouse_row][mouse_coll - 1] == "T":
                matrix[mouse_row][mouse_coll] = "*"
                matrix[mouse_row][mouse_coll - 1] = "M"
                print("Mouse is trapped!")
                break
            elif matrix[mouse_row][mouse_coll - 1] == "C":
                total_cheeses -= 1
            mouse_coll -= 1
            matrix[mouse_row][mouse_coll] = "M"
            matrix[mouse_row][mouse_coll + 1] = "*"
        else:
            print("No more cheese for tonight!")
    if command == "right":
        if position_valid(mouse_row, mouse_coll + 1, N, M):
            if matrix[mouse_row][mouse_coll + 1] == "@":
                command = input()
                continue
            elif matrix[mouse_row][mouse_coll + 1] == "T":
                matrix[mouse_row][mouse_coll] = "*"
                matrix[mouse_row][mouse_coll + 1] = "M"
                print("Mouse is trapped!")
                break
            elif matrix[mouse_row][mouse_coll + 1] == "C":
                total_cheeses -= 1
            mouse_coll += 1
            matrix[mouse_row][mouse_coll] = "M"
            matrix[mouse_row][mouse_coll - 1] = "*"
        else:
            print("No more cheese for tonight!")
            break
    if command == "up":
        if position_valid(mouse_row - 1, mouse_coll, N, M):
            if matrix[mouse_row -1][mouse_coll] == "@":
                command = input()
                continue
            elif matrix[mouse_row - 1][mouse_coll] == "T":
                matrix[mouse_row][mouse_coll] = "*"
                matrix[mouse_row - 1][mouse_coll] = "M"
                print("Mouse is trapped!")
                break
            elif matrix[mouse_row- 1][mouse_coll] == "C":
                total_cheeses -= 1
            mouse_row -= 1
            matrix[mouse_row][mouse_coll] = "M"
            matrix[mouse_row + 1][mouse_coll] = "*"
        else:
            print("No more cheese for tonight!")
            break
    if command == "down":
        if position_valid(mouse_row + 1, mouse_coll, N, M):
            if matrix[mouse_row + 1][mouse_coll] == "@":
                command = input()
                continue
            elif matrix[mouse_row + 1][mouse_coll] == "T":
                matrix[mouse_row][mouse_coll] = "*"
                matrix[mouse_row + 1][mouse_coll] = "M"
                print("Mouse is trapped!")
                break
            elif matrix[mouse_row + 1][mouse_coll] == "C":
                total_cheeses -= 1
            mouse_row += 1
            matrix[mouse_row][mouse_coll] = "M"
            matrix[mouse_row - 1][mouse_coll] = "*"
        else:
            print("No more cheese for tonight!")
            break

    command = input()
for row in matrix:
    print("".join(row))



