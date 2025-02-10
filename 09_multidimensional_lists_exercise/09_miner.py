def is_position_valid(row,coll,size):
    return 0 <= row < size and 0 <= coll < size


n = int(input())

commands = input().split()

cur_row, cur_coll = 0,0
coal = 0
matrix = []

game_over = False

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "s":
            cur_row, cur_coll = r,c
        elif matrix[r][c] == "c":
            coal += 1

for command in commands:
    if command == "right":
        if is_position_valid(cur_row, cur_coll + 1, n):
            cur_coll += 1
    elif command == "left":
        if is_position_valid(cur_row, cur_coll - 1, n):
            cur_coll -= 1
    elif command == "up":
        if is_position_valid(cur_row - 1, cur_coll, n):
            cur_row -= 1
    elif command == "down":
        if is_position_valid(cur_row + 1, cur_coll, n):
            cur_row += 1

    if matrix[cur_row][cur_coll] == "c":
        matrix[cur_row][cur_coll] = "*"
        coal -= 1
        if coal == 0:
            print(f"You collected all coal! ({cur_row}, {cur_coll})")
            game_over = True
    if matrix[cur_row][cur_coll] == "e":
        print(f"Game over! ({cur_row}, {cur_coll})")
        game_over = True
if not game_over:
    print(f"{coal} pieces of coal left. ({cur_row}, {cur_coll})")