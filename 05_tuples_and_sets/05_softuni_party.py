guests = set()

for i in range(int(input())):
    code = input()
    guests.add(code)

while True:
    guest = input()
    if guest == "END":
        break
    guests.remove(guest)
sorted_guest = sorted(guests)
print(len(sorted_guest))
for g in sorted_guest:
    print(g)


