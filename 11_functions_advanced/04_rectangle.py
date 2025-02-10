def rectangle(length, wigth):
    if not isinstance(length,int) or not isinstance(wigth,int):
        return f"Enter valid values!"

    def area():
        return length * wigth
    def perimetar():
        return 2*(length +wigth)

    result = f"Rectangle area: {area()}\nRectangle perimeter: {perimetar()}"
    return (result)


print(rectangle(2, 10))