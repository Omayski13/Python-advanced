from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items_dict = {"Patch":0,"Bandage":0,"MedKit":0}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    current_sum = current_textile + current_medicament
    if current_sum == 30:
        items_dict["Patch"] += 1
    elif current_sum == 40:
        items_dict["Bandage"] += 1
    elif current_sum >= 100:
        items_dict["MedKit"] += 1
        if current_sum > 100:
            current_sum -= 100
            medicaments[-1] += current_sum
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")


sorted_dict = sorted(items_dict.items(),key=lambda x: (-(x[1]), x[0]))

for data in sorted_dict:
    if data[1] > 0:
        print(f"{data[0]} - {data[1]}")

if medicaments:
    sort_medicaments = medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")