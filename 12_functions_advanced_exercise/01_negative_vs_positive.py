# nums = [int(x) for x in input().split()]
# positive = []
# negative = []
# for num in nums:
#     if num < 0:
#         negative.append(num)
#     else:
#         positive.append(num)
#
# pos_sum = (sum(positive))
# neg_sum = (sum(negative))
# print(neg_sum)
# print(pos_sum)
#
# if abs(pos_sum) > abs(neg_sum):
#     print(f"The positives are stronger than the negatives")
# else:
#     print("The negatives are stronger than the positives")


def sum_nums(*args):
    neg_sum = 0
    pos_sum = 0
    for num in args:
        if num < 0:
            neg_sum += num
        else:
            pos_sum += num

    return neg_sum,pos_sum

nums = [int(x) for x in input().split()]

print(sum_nums(*nums)[0])
print(sum_nums(*nums)[1])

if abs(sum_nums(*nums)[0]) > (sum_nums(*nums)[1]):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
