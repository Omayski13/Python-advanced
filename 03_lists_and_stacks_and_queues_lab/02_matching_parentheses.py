text = list(input())
stack_parent = []

for index in range(len(text)):
    if text[index] == "(":
        stack_parent.append(index)
    elif text[index] == ")":
        removed_index = stack_parent.pop()
        print("".join(text[removed_index:index+1]))
