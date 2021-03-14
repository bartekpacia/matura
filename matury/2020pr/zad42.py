from typing import List

from reader import read_nums

# nums = read_nums()
nums = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]

longest_reg_fragment: List[int] = []

for i in range(len(nums) - 1):
    reg_fragment: List[int] = []

    for j in range(i + 1, len(nums)):
        num1 = nums[i]
        num2 = nums[j]

        gap = abs(num1 - num2)

        if not reg_fragment:
            reg_fragment.append(gap)

        if gap != reg_fragment:
            break

    if len(reg_fragment) > len(longest_reg_fragment):
        longest_reg_fragment = reg_fragment

first = longest_reg_fragment[0]
last = longest_reg_fragment[-1]
print(first, last, len(longest_reg_fragment))
