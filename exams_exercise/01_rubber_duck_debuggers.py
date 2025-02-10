from collections import deque

time = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]
darth_vader = 0
thor = 0
big_blue = 0
small_yellow = 0
while time and tasks:
    current_time = time.popleft()
    current_task = tasks.pop()
    current_sum = current_time * current_task
    if current_sum <= 60:
        darth_vader += 1
    elif 60 < current_sum <= 120:
        thor += 1
    elif 120 < current_sum <= 180:
        big_blue += 1
    elif 180 < current_sum <= 240:
        small_yellow += 1
    elif current_sum > 240:
        time.append(current_time)
        current_task -= 2
        tasks.append(current_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader}\nThor Ducky: {thor}\nBig Blue Rubber Ducky: {big_blue}\nSmall Yellow Rubber Ducky: {small_yellow}")


