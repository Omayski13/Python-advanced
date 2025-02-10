from collections import deque

monsters = deque([int(x) for x in input().split(',')])
soldier_attacks = [int(x) for x in input().split(',')]
killed_mosters = 0
while monsters and soldier_attacks:
    monster_def = monsters.popleft()
    soldier_att = soldier_attacks.pop()
    if soldier_att >= monster_def:
        killed_mosters += 1
        soldier_att -= monster_def
        if soldier_attacks:
            soldier_attacks[-1] += soldier_att
        if not soldier_attacks:
            if soldier_att != 0:
                soldier_attacks.append(soldier_att)
    else:
        monster_def -= soldier_att
        monsters.append(monster_def)

if not monsters:
    print("All monsters have been killed!")
if not soldier_attacks:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_mosters}")


