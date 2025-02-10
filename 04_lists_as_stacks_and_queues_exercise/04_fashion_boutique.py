from collections import deque

clothes = deque(int(x) for x in input().split())
rack_size = int(input())
racks = 1
current_rack_size = 0

while clothes:
    current_clothing =clothes[0]
    if (current_clothing + current_rack_size) > rack_size:
        racks += 1
        current_rack_size = 0
    else:
        current_rack_size += current_clothing
        clothes.popleft()

print(racks)

