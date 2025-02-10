from collections import deque

numbers = deque

for n in range(int(input())):
    number_data = [int(x) for x in input().split()]
    command = number_data[0]

    if command == "1":
        numbers.append(number_data[1])
    if command == "2":
        if numbers:
            numbers.pop()
    if command == "3":
        if numbers:
            print(max(numbers))
    if command == "4":
        if numbers:
            print(min(numbers))

print(numbers.reverse())

print(*numbers, sep=", ")