import math

with open("dane/liczby.txt") as f:
  lines = f.read().splitlines()


nums = [int(ln) for ln in lines if ln]

master_list = []
for i, num1 in enumerate(nums):
  local_list = []

  local_list.append(num1)
  for j in range(i + 1, len(nums)):
    num2 = nums[j]

    if math.gcd(*local_list, num2) > 1:
      local_list.append(num2)
    else:
      master_list.append(local_list)
      break

longest_list = max(master_list, key=len)
gcd_max = math.gcd(*longest_list)
length = len(longest_list)

first = longest_list[0]  # pierwsza liczba najdłuższego ciagu

print(f"pierwsza liczba ciagu {first}, długość {length}, nwd {gcd_max}")
