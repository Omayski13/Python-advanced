rows = int(input())
matrix = []

for i in range(rows):
    el = [int(x) for x in input().split()]
    matrix.append(el)
sum_el = 0
for i in range(rows):
    sum_el += matrix[i][i]
print(sum_el)