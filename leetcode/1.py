nums = [2, 7, 11, 15]

target = 9

rst = []

for i, n in enumerate(nums):
    cmp = target - n

    if cmp in nums:
        rst.append(i)
        rst.append(nums.index(cmp))
        break

print(rst)


