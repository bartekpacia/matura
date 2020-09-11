from typing import List

def fact(num) -> int:
  if num == 0 or num == 1:
    return 1
  return num * fact(num - 1)

def to_digits(num) -> List[int]:
  digits = []
  for char in str(num):
    digits.append(int(char))
  
  return digits

with open("dane/liczby.txt") as f:
  lines = f.read().splitlines()

nums = []

for ln in lines:
  if not ln:
    continue

  num = int(ln)

  facts_of_num = []
  num_digits = to_digits(num)
  for digit in num_digits:
    f = fact(digit)
    facts_of_num.append(f)

  if num == sum(facts_of_num):
    nums.append(num)


for num in nums:
  print(f"znaleziono {num}")