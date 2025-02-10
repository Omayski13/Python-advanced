from collections import deque

liters_in_dispenser = int(input())
name = input()

waiting_people = deque()

while name != 'Start':
    waiting_people.append(name)
    name = input()

name = input()
while name != "End":
    splitted_name = name.split()
    if splitted_name[0] == "refill":
        liters_in_dispenser += int(splitted_name[1])
    else:
        current_liters = int(name)
        if current_liters <= liters_in_dispenser:
            print(f"{waiting_people.popleft()} got water")
            liters_in_dispenser -= current_liters
        else:
            print((f"{waiting_people.popleft()} must wait"))

    name = input()

print(f"{liters_in_dispenser} liters left")