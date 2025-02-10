def start_spring(**kwargs):
    spring_dict = {}
    result = []
    for el,type in kwargs.items():
        if type not in spring_dict:
            spring_dict[type] = []
        spring_dict[type].append(el)
    sorted_spring = sorted(spring_dict.items(),key=lambda x: (-len(x[1]), x[0]))
    for type,elements in sorted_spring:
        result.append(f"{type}:\n")
        for element in sorted(elements):
            result.append(f"-{element}\n")

    return "".join(result)



example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

