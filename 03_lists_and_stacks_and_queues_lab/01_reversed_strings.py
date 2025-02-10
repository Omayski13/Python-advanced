text = list(input())
stack = []

for el in range(len(text)):
    stack.append(text.pop())

print("".join(stack))
