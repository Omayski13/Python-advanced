from collections import  deque


bows = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while bows and customers:
    current_bow = bows[-1]
    current_customer = customers[0]
    current_sum = abs(current_bow - current_customer)
    if current_bow == current_customer:
        bows.pop()
        customers.popleft()
    elif current_bow > current_customer:
        customers.popleft()
        bows[-1] -= current_customer
    elif current_customer > current_bow:
        bows.pop()
        customers[0] -= current_bow

if not customers:
    print("Great job! You served all the customers.")
    if bows:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bows])}")
if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")

# if not bows:
#     print("Out of ramen! You didn't manage to serve all customers.")
#     print(f"Customers left: {', '.join([str(x) for x in customers])}")
# else:
#     print("Great job! You served all the customers.")
#     if bows:
#         print(f"Bowls of ramen left: {', '.join([str(x) for x in customers])}")



    print()


