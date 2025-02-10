import sys

data = input().split(", ")
rows = int(data[0])
cols = int(data[1])
matrix = []

for i in range(int(data[0])):
    el = [int(x) for x in input().split(", ")]
    matrix.append(el)

maxi_num = -sys.maxsize

for i in range(int(data[0]) - 1):
    for j in range(int(data[1]) - 1):
        current_sum = matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
        if current_sum > maxi_num:
            maxi_num = current_sum
            maxi_matrix = [[matrix[i][j], matrix[i][j+1]], [matrix[i+1][j],matrix[i+1][j+1]]]
print(*maxi_matrix[0])
print(*maxi_matrix[1])
print(maxi_num)

