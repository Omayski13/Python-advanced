elements = set()
num = int(input())
for i in range(num):
    element = input().split()
    for el in element:
        elements.add(el)
print(*elements, sep='\n')