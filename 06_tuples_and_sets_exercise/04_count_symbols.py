word = tuple(input())

unique_elements = sorted(set(word))

for el in unique_elements:
    print(f"{el}: {word.count(el)} time/s")
