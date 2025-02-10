from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gifts = {'Gemstone': 0,
         'Porcelain Sculpture': 0,
         'Gold': 0,
         'Diamond Jewellery': 0}

while magic and materials:
    current_material = materials.pop()
    current_magic = magic.popleft()
    current_sum = current_magic + current_material
    if 100 <= current_sum < 200:
        gifts['Gemstone'] += 1
    elif 200 <= current_sum < 300:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= current_sum < 400:
        gifts['Gold'] += 1
    elif 400 <= current_sum < 500:
        gifts['Diamond Jewellery'] += 1
    elif current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_material + current_magic
        elif current_sum % 2 != 0:
            current_sum *= 2
        if 100 <= current_sum < 200:
            gifts['Gemstone'] += 1
        elif 200 <= current_sum < 300:
            gifts['Porcelain Sculpture'] += 1
        elif 300 <= current_sum < 400:
            gifts['Gold'] += 1
        elif 400 <= current_sum < 500:
            gifts['Diamond Jewellery'] += 1
    elif current_sum > 499:
        current_sum /= 2
        if 100 <= current_sum < 200:
            gifts['Gemstone'] += 1
        elif 200 <= current_sum < 300:
            gifts['Porcelain Sculpture'] += 1
        elif 300 <= current_sum < 400:
            gifts['Gold'] += 1
        elif 400 <= current_sum < 500:
            gifts['Diamond Jewellery'] += 1

sorted_gifts = dict(sorted(gifts.items(),key=lambda x: x[0]))

if sorted_gifts['Gemstone'] > 0 and sorted_gifts['Porcelain Sculpture'] > 0:
    print("The wedding presents are made!")
elif sorted_gifts['Gold'] > 0 and sorted_gifts['Diamond Jewellery'] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for gift,quantity in sorted_gifts.items():
    if quantity > 0:
        print(f"{gift}: {quantity}")






