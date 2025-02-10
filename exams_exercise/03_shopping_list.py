def shopping_list(start_budget,**kwargs):
    result = []
    shopping_cart = 0
    budget = start_budget
    for product,parameters in kwargs.items():
        price,quantity = parameters[0],parameters[1]
        if start_budget < 100:
            return f"You do not have enough budget.\n"
        if shopping_cart == 5:
            break
        if (price * quantity) > int(budget):
            continue
        result.append(f"You bought {product} for {(price * quantity):.2f} leva.\n")
        shopping_cart += 1
        budget -= (price*quantity)
    return "".join(result)




print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

