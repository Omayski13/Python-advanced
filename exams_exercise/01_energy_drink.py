from collections import  deque

miligrams_coffein = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

coffein = 0

while miligrams_coffein and energy_drinks:
    current_coffein = miligrams_coffein.pop()
    current_drink = energy_drinks.popleft()
    current_sum = current_coffein * current_drink
    if (current_sum + coffein) <= 300:
        coffein += current_sum
    else:
        energy_drinks.append(current_drink)
        if coffein >= 30:
            coffein -= 30
        else:
            coffein = 0
if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {coffein} mg caffeine.")