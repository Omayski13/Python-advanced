def shop_from_grocery_list(budget,list,*args):
    purchased_product = []
    result = []
    for data in args:
        product = data[0]
        price = float(data[1])
        if price > budget:
            break
        if product in purchased_product:
            continue
        if product not in list:
            continue
        if price <= budget:
            budget -= price
            purchased_product.append(product)
            list.remove(product)
    if not list:
        result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        result.append(f"You did not buy all the products. Missing products: {', '.join(list)}.")
    return "".join(result)

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
