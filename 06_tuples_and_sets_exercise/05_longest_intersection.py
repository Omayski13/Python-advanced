num = int(input())
longest_intersection = set()

for i in range(num):
    first, second = input().split("-")
    first = str(first)
    second = str(second)
    f_start, f_end = first.split(",")
    s_start, s_end = second.split(",")
    f_set = set()
    s_set = set()
    for f in range(int(f_start),int(f_end) + 1):
        f_set.add(f)
    for s in range(int(s_start),int(s_end) + 1):
        s_set.add(s)
    current_intersection = set(f_set & s_set)
    if longest_intersection:
        if len(current_intersection) > len(longest_intersection):
            longest_intersection = current_intersection
    else:
        longest_intersection = current_intersection
print(f"Longest intersection is {[num for num in longest_intersection]} with length {len(longest_intersection)}")