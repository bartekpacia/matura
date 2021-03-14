from reader import read_nums

nums = read_nums()

biggest_gap: int = None
smallest_gap: int = None

for i in range(1, len(nums)):
    num1 = nums[i - 1]
    num2 = nums[i]

    gap = abs(num1 - num2)

    if not biggest_gap:
        biggest_gap = gap

    if not smallest_gap:
        smallest_gap = gap

    if gap > biggest_gap:
        biggest_gap = gap

    if gap < smallest_gap:
        smallest_gap = gap

print(f"{smallest_gap=}, {biggest_gap=}")
