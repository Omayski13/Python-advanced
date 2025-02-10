def concatenate(*args,**kwargs):
    my_string = ''
    for el in args:
        my_string += el
    for key,value in kwargs.items():
        if key in my_string:
            my_string = my_string.replace(key,value)
    result = ''.join(my_string)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
