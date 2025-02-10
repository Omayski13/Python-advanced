lines = int(input())
stack = []

for n in range(lines):
    command = input()
    splitted_command = command.split()
    f_command = splitted_command[0]
    if f_command == "1":
        stack.append(int(splitted_command[1]))
    elif f_command == "2":
        if stack:
            stack.pop()
    elif f_command == "3":
        if stack:
            print(max(stack))
    elif f_command == "4":
        if stack:
            print(min(stack))
new_stack = []
while stack:
    new_stack.append(str(stack.pop()))
print(", ".join(new_stack))