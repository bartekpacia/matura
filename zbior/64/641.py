from typing import List

file = open("dane_obrazki.txt", "r")

zeros = 0
ones = 0
max_ones = 0
img_index = 0

rewersy = 0
for line_i, line in enumerate(file.readlines()):
  fmt_line = line.strip()[:-1]

  if fmt_line == "":
    print(f"empty line at {line_i+1}")
    if ones > zeros:
      rewersy += 1

    if ones > max_ones:
      max_ones = ones
      print(f"new max ones at line {line_i+1}")

    zeros = 0
    ones = 0
    img_index += 1
    continue

  elif len(fmt_line) != 20:
    continue

  for char in fmt_line:
    if char == "1":
      ones += 1
    elif char == "0":
      zeros += 1
    else:
      print("bad")
  

file.close()

print(f"liczba rewersów: {rewersy}")
print(f"najwięcej czarnych pikseli: {max_ones}")
