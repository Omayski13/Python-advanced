number = int(input())
cars = set()

for n in range(number):
    command, plate = input().split(", ")
    if command == "IN":
        cars.add(plate)
    elif command == "OUT":
        if plate in cars:
            cars.remove(plate)

if cars:
    for car_plate in cars:
        print(car_plate)
else:
    print("Parking Lot is Empty")