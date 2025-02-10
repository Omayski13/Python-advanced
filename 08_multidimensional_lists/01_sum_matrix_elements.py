# rows,cols = input().split(", ")
#
# matrix = []
# sum_num = 0
#
# for row_index in range(int(rows)):
#     elements = [int(x) for x in input().split(", ")]
#     sum_num += sum(elements)
#     matrix.append(elements)
#
# print(sum_num)
# print(matrix)


n,c = input().split(", ")

sum_matrix = 0
matrix = [[int(x) for x in input().split(", ")]for _ in range(int(n))]
for i in range(int(n)):
    sum_matrix += sum(matrix[i])

print(sum_matrix)
print(matrix)

