first = set(int(num) for num in input().split())
second = set(int(num) for num in input().split())
num = int(input())

for i in range(num):
    line = input().split()
    command = line[0] + " " + line[1]
    nums = [int(num) for num in line[2:]]
    if command == "Add First":
        first.update(nums)
    elif command == "Add Second":
        second.update(nums)
    elif command == "Remove First":
        first.difference_update(nums)
    elif command == "Remove Second":
        second.difference_update(nums)
    else:
        print(first.issubset(second) or second.issubset(first))
print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")

