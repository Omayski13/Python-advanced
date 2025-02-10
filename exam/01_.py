from collections import deque

fuel = [int(x) for x in input().split()]
consumtion_index = deque([int(x) for x in input().split()])
quantities = deque([int(x) for x in input().split()])
altitude = 1
altitudes = []
failed = False

while fuel:
    current_fuel = fuel.pop()
    current_consumtion_index = consumtion_index.popleft()
    current_quantites = quantities.popleft()
    current_sum = current_fuel - current_consumtion_index

    if current_sum >= current_quantites:
        print(f"John has reached: Altitude {altitude}")
        altitudes.append(f"Altitude {altitude}")
        altitude += 1
    elif current_sum < current_quantites:
        print(f"John did not reach: Altitude {altitude}")
        failed = True
        break

if failed:
    print("John failed to reach the top.")
    if altitude == 1:
        print("John didn't reach any altitude.")
    if altitude > 1:
        print(f"Reached altitudes: {', '.join([str(x) for x in altitudes])}")
else:
    print("John has reached all the altitudes and managed to reach the top!")


