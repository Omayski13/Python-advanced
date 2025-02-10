data = input().split()
matrix = []

for i in range(int(data[0])):
    el = [x for x in input().split()]
    matrix.append(el)
identical = 0
for i in range(int(data[0])-1):
    for j in range(int(data[1])-1):
        if matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i+1][j+1] and matrix[i][j]== matrix[i+1][j] and matrix[i][j] == matrix[i+1][j+1]:
            identical += 1

print(identical)

