def shopping_cart(*args):
    shopping = {"Pizza":[],"Dessert":[],"Soup":[]}
    dessert = 2
    pizza = 4
    soup = 3

    for data in args:
        if data == "Stop":
            break

        if data[0] == "Pizza":
            if len(shopping[data[0]])<4:
                if data[1] not in shopping[data[0]]:
                    shopping[data[0]].append(data[1])
        if data[0] == "Soup":
            if len(shopping[data[0]])<3:
                if data[1] not in shopping[data[0]]:
                    shopping[data[0]].append(data[1])
        if data[0] == "Dessert":
            if len(shopping[data[0]])<2:
                if data[1] not in shopping[data[0]]:
                    shopping[data[0]].append(data[1])
    result = []
    for value in shopping.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'
    sorted_shopping = sorted(shopping.items(),key=lambda x: (-len(x[1]),x[0]))
    for data in sorted_shopping:
        result.append(f"{data[0]}:\n")
        sorted_products = sorted(data[1])
        for product in sorted_products:
            result.append(f" - {product}\n")
    return "".join(result)

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))




