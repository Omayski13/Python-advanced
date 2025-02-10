nums = [float(x) for x in input().split()]
nums_tuple = tuple(nums)
printed_nums = []

for num in nums_tuple:
    if num not in printed_nums:
        print(f"{num:.1f} - {nums_tuple.count(num)} times")
        printed_nums.append(num)