def even_odd_filter(**kwargs):

    for command,nums in kwargs.items():
        if command == "even":
            kwargs[command] = list(filter(lambda x: x % 2 == 0, nums))
        if command == "odd":
            kwargs[command] = list(filter(lambda x: x % 2 != 0, nums))

    return dict(sorted(kwargs.items(),key=lambda kvp: -len(kvp[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
