import sys

data = input().split()
matrix = []

for i in range(int(data[0])):
    el = [int(x) for x in input().split()]
    matrix.append(el)


max_num = -sys.maxsize
for i in range(int(data[0])-2):
    for j in range(int(data[1])-2):
        current_num = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j]+ matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if current_num > max_num:
            max_num = current_num
            max_matrix = [[matrix[i][j], matrix[i][j+1], matrix[i][j+2]],[matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]],[matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]]

print(f"Sum = {max_num}")
print(*max_matrix[0])
print(*max_matrix[1])
print(*max_matrix[2])