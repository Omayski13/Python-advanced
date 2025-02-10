def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp:(-len(kvp[1]), kvp[0]))
    result =''

    for name, quantites in sorted_dict:
        result += f"{name}\n"
        sorted_qunatities = sorted(quantites,reverse=True)
        result += "\n".join([str(el) for el in quantites])
        result += "\n"

    return result
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
