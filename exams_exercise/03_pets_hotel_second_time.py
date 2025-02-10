def accommodate_new_pets(capacity,max_weight,*args):
    result = []
    accommodated_pets = 0
    full_hotel = False
    animals = {}
    for pet,weight in args:
        pet = pet
        weight = float(weight)
        if capacity == 0:
            full_hotel = True
            break
        if weight > max_weight:
            continue
        if pet not in animals:
            animals[pet] = 0
        animals[pet] += 1
        capacity -= 1
        accommodated_pets += 1
    if not full_hotel:
        result.append(f"All pets are accommodated! Available capacity: {capacity }.\n")
    if full_hotel:
        result.append("You did not manage to accommodate all pets!\n")
    sorted_animals = dict(sorted(animals.items(),key=lambda x: x[0]))
    result.append("Accommodated pets:\n")
    for pet,amount in sorted_animals.items():
        result.append(f"{pet}: {amount}\n")
    return "".join(result)





print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


