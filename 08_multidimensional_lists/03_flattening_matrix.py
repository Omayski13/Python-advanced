rows = int(input())
matrix = []

for row_index in range(rows):
    el = [int(x) for x in input().split(", ")]
    matrix.append(el)

flattened_list = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattened_list.append(matrix[row_index][col_index])
print(flattened_list)


