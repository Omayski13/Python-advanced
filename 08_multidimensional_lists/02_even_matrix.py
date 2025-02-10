# rows = int(input())
#
# matrix = []
#
# for row_index in range(rows):
#     el = [int(x) for x in input().split(", ")]
#     matrix.append(el)
#
# even_matrix = []
# for row_index in range(rows):
#     even_matrix.append([])
#     for col_index in range(len(matrix[row_index])):
#         if matrix[row_index][col_index] % 2 == 0:
#             even_matrix[row_index].append(matrix[row_index][col_index])
# print(even_matrix)




rows = int(input())
matrix = []

for row_index in range(rows):
    el = [int(x) for x in input().split(', ')]
    matrix.append(el)

even_matrix = []
for row_index in range(rows):
    even_matrix.append([])
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] % 2 == 0:
            even_matrix[row_index].append(matrix[row_index][col_index])
print(even_matrix)
