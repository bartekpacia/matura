import math


def to_digits(num: int) -> list[int]:
    digits: list[int] = []
    for char in str(num):
        digits.append(int(char))

    return digits


with open("dane/liczby.txt") as f:
    lines = f.read().splitlines()

nums: list[int] = []

for line in lines:
    if not line:
        continue

    num = int(line)

    facts_of_num: list[int] = []
    num_digits = to_digits(num)
    for digit in num_digits:
        f = math.factorial(digit)
        facts_of_num.append(f)

    if num == sum(facts_of_num):
        nums.append(num)

for num in nums:
    print(f"znaleziono {num}")
