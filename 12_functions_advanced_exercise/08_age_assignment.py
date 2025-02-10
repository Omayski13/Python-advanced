def age_assignment(*args,**kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]
    result = sorted(persons.items(),key=lambda x: x[0])
    res = []
    for name,age in result:
        res.append(f"{name} is {age} years old.")
    return "\n".join(res)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))