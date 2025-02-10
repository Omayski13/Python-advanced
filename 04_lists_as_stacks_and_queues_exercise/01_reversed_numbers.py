my_list = list(input().split())
my_stack = []

while my_list:
    my_stack.append(my_list.pop())

print(" ".join(my_stack))