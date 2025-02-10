my_list = [x for x in input().split("|")]

for index in range(len(my_list)):
    [int(num) for num in my_list[index] if num != " "]
