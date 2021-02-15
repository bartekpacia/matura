n = 45788

w = 0
while n != 0:
  w = w + (n % 10)
  n = n // 10

print(f"{w=}")
