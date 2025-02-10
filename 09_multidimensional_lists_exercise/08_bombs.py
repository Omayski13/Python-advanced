def valid_cell(row,coll, size):
    return 0 <= row < size and 0<= coll < size

n = int(input())
matrix = []
for r in range(n):
    elements = [int(el) for el in (input().split())]
    matrix.append(elements)

bombs = input().split()

for bomb in bombs:
    bomb_row = int(bomb[0])
    bomb_coll = int(bomb[2])

    bomb_value = matrix[bomb_row][bomb_coll]

    for row_index in range(bomb_row - 1, bomb_row + 2):
        for col_index in range(bomb_coll - 1, bomb_coll + 2):
            if valid_cell(row_index,col_index,n):
                if matrix[row_index][col_index] > 0:
                    matrix[row_index][col_index] -= bomb_value
        matrix[bomb_row][bomb_coll] = 0

alive_cells = 0
sum_of_cells = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            alive_cells += 1
            sum_of_cells += matrix[r][c]
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
for row in matrix:
    print(*row)


