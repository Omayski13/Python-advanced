n = int(input())
matrix = []
# matrix = [[el for el in input().split()]for _ in range(n)]

bunny_row,bunny_col = 0,0
for r in range(n):
    c = -1
    elements = input().split()
    matrix.append(elements)
    for el in elements:
        c += 1
        if el == "B":
            bunny_row,bunny_col = r,c

left_indexes = []
left = []
right_indexes = []
right = []
up_indexes = []
up = []
down_indexes = []
down = []

for right_el_index in range(bunny_col+1,n):
    if matrix[bunny_row][right_el_index] != "X":
        if int(matrix[bunny_row][right_el_index]) > 0:
            right_index = [bunny_row,right_el_index]
            right_indexes.append(right_index)
            right.append(int(matrix[bunny_row][right_el_index]))
for down_el_index in range(bunny_row +1, n):
    if matrix[down_el_index][bunny_col] != "X":
        if int(matrix[down_el_index][bunny_col]) > 0:
            down_index = [down_el_index,bunny_col]
            down_indexes.append(down_index)
            down.append(int(matrix[down_el_index][bunny_col]))
for left_el_index in range(bunny_col - 1,0, -1):
    if matrix[bunny_row][left_el_index] != "X":
        if int(matrix[bunny_row][left_el_index]) > 0:
            left_index = [bunny_row,left_el_index]
            left_indexes.append(left_index)
            left.append(int(matrix[bunny_row][left_el_index]))
for up_el_index in range(bunny_row -1 ,0, -1 ):
    if matrix[up_el_index][bunny_col] != "X":
        if int(matrix[up_el_index][bunny_col]) > 0:
            up_index = [up_el_index,bunny_col]
            up_indexes.append(up_index)
            up.append(int(matrix[up_el_index][bunny_col]))


biggest_sum = max(sum(left),sum(right),sum(down),sum(up))
if biggest_sum == sum(left):
    print("left")
    print(*left_indexes, sep="\n")
elif biggest_sum == sum(right):
    print("right")
    print(*right_indexes, sep="\n")
elif biggest_sum == sum(down):
    print("down")
    print(*down_indexes, sep="\n")
elif biggest_sum == sum(up):
    print("up")
    print(*up_indexes, sep="\n")
print(biggest_sum)


# print(f"left{left}")
# print(f"left{left_indexes}")
# print(f"right{right}")
# print(f"right{right_indexes}")
# print(f"up{up}")
# print(f"up{up_indexes}")
# print(f"down{down}")
# print(f"down{down_indexes}")