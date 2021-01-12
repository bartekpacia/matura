from typing import List

file = open("dane_obrazki.txt", "r")

max_zeros = 0
zeros = 0
ones = 0
i = 0

rewersy = 0
for line in file.readlines():
  fmt_line = line.strip()[:-1]

  if fmt_line == "":
    if ones > zeros:
      print(f"{i} jest rewersem")
      rewersy += 1
    else:
      print(f"{i} NIE jest rewersem")

    if zeros > max_zeros:
      max_zeros = zeros

    zeros = 0
    ones = 0
    i += 1
    continue

  if len(fmt_line) != 20:
    print("invalid length of a line!")
    continue

  for char in fmt_line:
    if char == '1':
      ones += 1
    elif char == "0":
      zeros += 1
    else:
      print("bad")
  

file.close()

print(f"liczba rewersów: {rewersy}")
print(f"najwięcej czarnych pikseli: {max_zeros}")
