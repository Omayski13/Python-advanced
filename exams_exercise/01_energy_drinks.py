from collections import deque

coffein = [int(x) for x in input().split(", ")]
drinks = deque([int(x) for x in input().split(", ")])

stamat_coffein = 0

while coffein and drinks:
    current_coffein = coffein.pop()
    current_drink = drinks.popleft()
    current_sum = current_drink * current_coffein
    if (current_sum+stamat_coffein) > 300:
        drinks.append(current_drink)
        stamat_coffein -= 30
        if stamat_coffein < 0:
            stamat_coffein =0
    else:
        stamat_coffein += current_sum

if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_coffein} mg caffeine.")