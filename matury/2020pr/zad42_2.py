from typing import List

from reader import read_nums

# nums = read_nums()
nums = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]

longest_reg_fragment: List[int] = []
reg_fragment: List[int] = []

current_gap = nums[1] - nums[0]
for i in range(1, len(nums)):
    num1 = nums[i - 1]
    num2 = nums[i]

    gap = abs(num1 - num2)
    print(f"gap between {num1} (i={i - 1}) and {num2} (i={i}) = {gap}")

    if not reg_fragment:
        reg_fragment.append(num1)

    if gap == current_gap:
        reg_fragment.append(num2)
    else:
        if len(reg_fragment) > len(longest_reg_fragment):
            print(f"len {reg_fragment} > len {longest_reg_fragment}")
            longest_reg_fragment = reg_fragment.copy()

        current_gap = gap
        reg_fragment.clear()

first = longest_reg_fragment[0]
last = longest_reg_fragment[-1]
print(f"f{longest_reg_fragment=}")
print(first, last, len(longest_reg_fragment))
