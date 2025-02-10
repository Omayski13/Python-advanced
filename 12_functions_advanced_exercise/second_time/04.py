def even_odd_filter(**kwargs):
    for command,value in kwargs.items():
        if command == "even":
            kwargs[command] = list(filter(lambda x: x % 2 == 0, value))
        if command == "odd":
            kwargs[command] = list(filter(lambda x: x % 2 != 0, value))
    result = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    return result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
