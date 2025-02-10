from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbol = deque((x) for x in input().split())
honey = 0


while len(bees) > 0 and len(nectar) > 0 and len(symbol) > 0:
    current_bee = bees[0]
    current_nectar = nectar[-1]
    current_symbol = symbol[0]
    while current_nectar >= current_bee:
        if current_symbol == "+":
            honey += abs(current_bee + current_nectar)
            bees.popleft()
            nectar.pop()
            symbol.popleft()
            break
        elif current_symbol == "-":
            honey += abs(current_bee - current_nectar)
            bees.popleft()
            nectar.pop()
            symbol.popleft()
            break
        elif current_symbol == "*":
            honey += abs(current_bee * current_nectar)
            bees.popleft()
            nectar.pop()
            symbol.popleft()
            break
        elif current_symbol == "/":
            if current_nectar == 0:
                bees.popleft()
                nectar.pop()
                symbol.popleft()
                continue
            else:
                honey += abs(current_bee / current_nectar)
                bees.popleft()
                nectar.pop()
                symbol.popleft()
                break
    else:
        nectar.pop()


print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(el) for el in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(el) for el in nectar])}")

