from collections import deque

material = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())
christmas = False
doll = 0
train = 0
bear = 0
cycle = 0


while True:
    if len(material) < 1 or len(magic) < 1:
        break
    if magic[0] == 0 and material[-1] == 0:
        material.pop()
        magic.popleft()
        continue
    if material[-1] == 0:
        material.pop()
        continue
    if magic[0] == 0:
        magic.popleft()
        continue

    if doll > 0 and train > 0:
        christmas = True
    if bear > 0 and cycle > 0:
        christmas = True

    magic_level =(material[-1])*(magic[0])
    if magic_level == 150:
        doll += 1
        material.pop()
        magic.popleft()
    elif magic_level == 250:
        train += 1
        material.pop()
        magic.popleft()
    elif magic_level == 300:
        bear += 1
        material.pop()
        magic.popleft()
    elif magic_level == 400:
        cycle += 1
        material.pop()
        magic.popleft()
    else:
        if magic_level < 0:
            negative_magic = (material[-1])+(magic[0])
            material.pop()
            magic.popleft()
            material.append(negative_magic)
        else:
            current_material = material[-1]
            magic.popleft()
            material.pop()
            material.append(current_material + 15)

if christmas:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material:
    material = reversed(material)
    print(f"Materials left: {', '.join([str(x) for x in material])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

present = {}
if doll:
    present["Doll"] = doll
if train:
    present["Wooden train"] = train
if bear:
    present["Teddy bear"] = bear
if cycle:
    present["Bicycle"] = cycle

sorted_toys = {key: value for key, value in sorted(present.items())}
for item, quantity in sorted_toys.items():
    print(f'{item}: {quantity}')



