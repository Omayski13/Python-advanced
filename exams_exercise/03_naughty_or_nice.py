from collections import deque

def naughty_or_nice_list(list, *args,**kwargs):
    list = deque(list)
    new_list =
    result = []
    kids_dict = {}
    nice = []
    naughty = []
    not_found = []
    my_dict = {"Nice":[], "Naughty":[], "Not found":[]}
    for num,name in list:
        kids_dict[num]=name
    for el in args:
        el = el.split("-")
        num = int(el[0])
        direction=el[1]
        for data in list:
            number = data[0]
            name = data[1]
            if number == num:
                if direction == "Nice":
                    nice.append(name)
                elif direction == "Naughty":
                    naughty.append(name)
            list.popleft()
    if kwargs:
        for name,direction in kwargs.items():
            new_dict = {v: k for v, k in kids_dict.items()}
            if name in new_dict:
                if direction == "Nice":
                    nice.append(name)
                elif direction == "Naughty":
                    naughty.append(name)
                new_dict.pop(name)




print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
