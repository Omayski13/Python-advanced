from collections import deque

food = int(input())
orders_left = False
orders = deque(int(x) for x in input().split())
print(max(orders))

while orders:
    current_order = orders[0]
    if food >= current_order:
        orders.popleft()
        food -= current_order
    else:
        orders_left = True
        break
if orders_left:
    orders_left_list= []
    while orders:
        orders_left_list.append(str(orders.popleft()))
    print(f'Orders left: {" ".join(orders_left_list)}')
else:
    print("Orders complete")
