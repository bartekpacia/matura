from typing import List

from reader import read_nums

nums = read_nums()

longest_reg_fragment: List[int] = []
reg_fragment: List[int] = []

current_gap = nums[1] - nums[0]
for i in range(1, len(nums)):
    num1 = nums[i - 1]
    num2 = nums[i]
    gap = abs(num1 - num2)

    if not reg_fragment:
        reg_fragment.append(num1)
        continue

    if gap == current_gap:
        reg_fragment.append(num1)
        continue

    if gap != current_gap:
        reg_fragment.append(num1)
        if len(reg_fragment) > len(longest_reg_fragment):
            longest_reg_fragment = reg_fragment.copy()

        current_gap = gap
        reg_fragment = [num1]

first = longest_reg_fragment[0]
last = longest_reg_fragment[-1]
print(first, last, len(longest_reg_fragment))
