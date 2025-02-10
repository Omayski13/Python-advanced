from collections import deque

name = input()
customers = deque()
while True:
    if name == "Paid":
        while customers:
            print(customers.popleft())
    elif name == "End":
        print(f"{len(customers)} people remaining.")
        break
    else:
        customers.append(name)

    name = input()