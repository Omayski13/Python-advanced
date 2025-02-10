from collections import deque

expression = [x for x in input().split()]
numbers = deque()


for el in expression:
    if el not in "+-/*":
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            f_num = numbers.popleft()
            s_num = numbers.popleft()
            if el == "+":
                numbers.appendleft(f_num + s_num)
            elif el == "-":
                numbers.appendleft(f_num - s_num)
            elif el == "/":
                numbers.appendleft(f_num // s_num)
            elif el == "*":
                numbers.appendleft(f_num * s_num)

print(*numbers)


