data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for row_index in range(int(data[0])):
    el = [int(x) for x in input().split()]
    matrix.append(el)


for col_index in range(cols):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)




