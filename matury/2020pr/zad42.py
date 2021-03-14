from reader import read_nums

nums = read_nums()

for i in range(len(nums) - 1):

    for j in range(i + 1, len(nums)):
        num1 = nums[i]
        num2 = nums[j]

        gap = abs(num1 - num2)
    