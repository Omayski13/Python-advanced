from collections import deque

chocolate = ([int(num) for num in input().split(", ")])
milk = ([int(num) for num in input().split(", ")])
chocolate = deque(chocolate)
milk = deque(milk)
not_enough = False

milkshakes = 0
while milkshakes != 5:
    if len(chocolate) < 1 or len(milk) < 1:
        not_enough = True
        break
    if len(chocolate) < 0 or len(milk) < 0:
        chocolate.remove(chocolate[-1])
        milk.remove(milk[0])
    if chocolate[-1] < 0:
        chocolate.remove(chocolate[-1])
        continue
    if milk[0] < 0:
        milk.remove(milk[0])
        continue
    elif chocolate[-1] == milk[0]:
        milkshakes +=1
        chocolate.pop()
        milk.popleft()
    else:
        chocolate[-1] -= 5
        milk.rotate(-1)



if not_enough:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")
if chocolate:
    print(f"Chocolate: {', '.join([str(el) for el in chocolate])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(el) for el in milk])}")
else:
    print("Milk: empty")



