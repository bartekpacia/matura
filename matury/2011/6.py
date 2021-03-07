from typing import List

with open("dane/liczby.txt") as f:
    nums: List[int] = []
    nums_9_chars: List[int] = []
    for line in f:
        sline = line.strip()
        num = int(sline, 2)

        if len(sline) == 9:
            nums_9_chars.append(num)

        nums.append(num)

count_even = 0
max_num = 0

for num in nums:
    if num % 2 == 0:
        count_even += 1

    if num > max_num:
        max_num = num

print(f"{count_even=}")
print(f"max_num(10): {max_num}, max_num(2): {bin(max_num)[2:]}")

sum_9_chars = 0
for num in nums_9_chars:
    sum_9_chars += num

print(f"count of numbers with 9 digits: {len(nums_9_chars)}, their sum: {bin(sum_9_chars)[2:]}")
