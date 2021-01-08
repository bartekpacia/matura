with open("przyklad623_1.txt") as f:
  liczby1 = [int(l, 8) for l in f.readlines()]

with open("przyklad623_2.txt") as f:
  liczby2 = [int(l, 10) for l in f.readlines()]

print(len(liczby1), len(liczby2))

same_value_in_same_rows = 0
first_value_bigger = 0
for i in range(len(liczby1)):
  num1 = liczby1[i]
  num2 = liczby2[i]

  if num1 == num2:
    same_value_in_same_rows += 1

  if num1 > num2:
    first_value_bigger += 1

print(f"{same_value_in_same_rows=}, {first_value_bigger=}")
