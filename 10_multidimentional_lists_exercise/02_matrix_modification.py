n = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(n)]

while True:
    data = input()
    if data == "END":
        break
    data = data.split()
    command = data[0]
    row,col,value = [int(x) for x in data[1:]]

    if 0 <= row < n and 0<= col < n:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
         print("Invalid coordinates")

for row in matrix:
    print(*row)


