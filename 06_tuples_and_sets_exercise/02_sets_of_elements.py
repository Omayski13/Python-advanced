f_set = set()
s_set = set()
f_set_lengt, s_set_lengt = input().split()

for i in range(int(f_set_lengt)):
    num = input()
    f_set.add(num)
for n in range(int(s_set_lengt)):
    num = input()
    s_set.add(num)

result = (f_set & s_set)
for el in result:
    print(el)

