with open("dane/liczby.txt") as f:
  lines = f.readlines()

wynik4 = open("wynik4.txt", "w")

count = 0
for line in lines:
  zeros = 0
  ones = 0

  for char in line.strip():
    if char == "0":
      zeros += 1
    elif char == "1":
      ones += 1

  if zeros > ones:
    count += 1

wynik4.write(f"zadanie 4.1: {count} liczb ma wiecej zer niz jedynek")