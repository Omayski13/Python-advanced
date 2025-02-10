def player_won(c_row,c_coll,matrix_rows,matrix_colls):
    return 0 > c_row or c_row > matrix_rows or 0 > c_coll or c_row > matrix_colls

def valid_idex(c_row,c_coll,matrix_rows,matrix_colls):
    return 0 <= c_row < matrix_rows or 0 <= c_coll < matrix_colls

game_won = False
game_loose = False

data = input().split()
n, m = int(data[0]),int(data[1])

matrix = []
p_row,p_coll = 0,0

for r in range(n):
    elements = input()
    matrix.append([])
    c = -1
    for el in elements:
        c += 1
        if el == "P":
            p_row,p_coll = r,c
        matrix[r].append(el)

commands = input()

for command in commands:
    matrix[p_row][p_coll] = "."
    if game_won or game_loose:
        break
    if command == "L":
        if player_won(p_row,p_coll - 1,n,m):
            game_won = True
        else:
            p_coll -= 1
    if command == "R":
        if player_won(p_row, p_coll + 1, n, m):
            game_won = True
        else:
            p_coll += 1
    if command == "U":
        if player_won(p_row - 1, p_coll, n, m):
            game_won = True
        else:
            p_coll -= 1
    if command == "D":
        if player_won(p_row + 1, p_coll, n, m):
            game_won = True
        else:
            p_coll += 1

    bunnies_count = 0
    bunnies_positions = []
    bunny_row,bunny_col = 0,0
    for row in range(n):
        for coll in range(m):
            if matrix[row][coll] == "B":
                bunnies_positions.append([])
                bunnies_positions[bunnies_count].append(row)
                bunnies_positions[bunnies_count].append(coll)
                bunnies_count += 1

    for bunny in range(bunnies_count):
        bunny_row,bunny_col = bunnies_positions[bunny][0],bunnies_positions[bunny][1]
        if valid_idex(bunny_row -1,bunny_col,n,m):
            matrix[bunny_row-1][bunny_col] = "B"
        if valid_idex(bunny_row, bunny_col-1, n, m):
            matrix[bunny_row][bunny_col - 1] = "B"
        if valid_idex(bunny_row, bunny_col+1, n, m):
            matrix[bunny_row][bunny_col + 1] = "B"
        if valid_idex(bunny_row+1, bunny_col, n, m):
            matrix[bunny_row +1][bunny_col] = "B"

for row in matrix:
    print("".join(row))
if game_won:
    print(f"won: {p_row} {p_coll}")
if game_loose:
    print(f"dead: {p_row} {p_coll}")

