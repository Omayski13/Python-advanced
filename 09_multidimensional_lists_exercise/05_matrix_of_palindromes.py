r,c = [int(x) for x in input().split()]

word = int(ord("a"))
matrix = []
for row in range(r):
    for coll in range(c):
        print(f"{chr(word + row)}{chr(word + row + coll)}{chr(word + row)}",end=" ")
    print()



