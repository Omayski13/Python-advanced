def age_assignment(*args,**kwargs):
    persons = {}
    for name,age in kwargs.items():
        persons[name] = age
    for arg_name in args:
        persons[arg_name] = persons.pop(arg_name[0])

    sorted_person = ""
    sorted_person = dict(sorted(persons.items(),key=lambda x: x))
    result = []
    for sorted_name,sorted_age in sorted_person.items():
        result.append(f"{sorted_name} is {sorted_age} years old.")
    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
