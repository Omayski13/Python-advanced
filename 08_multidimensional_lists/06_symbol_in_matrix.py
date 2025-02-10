rows = int(input())
matrix = []
for i in range(rows):
    el = list(input())
    matrix.append(el)

searched_el = input()
found = False
for i in range(rows):
    if found:
        break
    for j in range(len(matrix[i])):
        if searched_el == matrix[i][j]:
            print(f"({i}, {j})")
            found = True
            break

if not found:
    print(f"{searched_el} does not occur in the matrix")