def shop_from_grocery_list(budget,shopping_list,*args):
    for product,price in args:
        if product not in shopping_list:
            continue
        if int(price) > budget:
            break
        shopping_list.remove(product)
        budget -= price
    if len(shopping_list) == 0:
            return (f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        return (f"You did not buy all the products. Missing products: {', '.join(shopping_list)}.")


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))









