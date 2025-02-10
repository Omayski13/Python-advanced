from collections import deque

names = deque(input().split())
rotations = int(input()) -1

while len(names) > 1:
    names.rotate(-rotations)
    removed_kid = names.popleft()
    print(f"Removed {removed_kid}")
print(f"Last is {names.pop()}")