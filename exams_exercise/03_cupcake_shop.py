from collections import deque


def stock_availability(*args):
    result = []
    inventory = deque(args[0])
    command = args[1]
    if command == "delivery":
        for index in range(2,len(args)):
            inventory.append(args[index])
    if command == "sell":
        if args[2]:
            sell_argument = args[2]
            sell_argument_digit = sell_argument.isdigit()
            if sell_argument_digit == True:
                for index in range(int(args[2])):
                    inventory.popleft(index)





    result.append(inventory)

    return result

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))

print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

