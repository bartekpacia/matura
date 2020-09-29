def decompose(num: int) -> []:
  factors = []
  k = 2

  while num > 1:
    while num % k == 0:
      factors.append(k)
      num = num // k

    k = k + 1

  return factors


print(f"{decompose(2)=}")
print(f"{decompose(3)=}")
print(f"{decompose(4)=}")
print(f"{decompose(5)=}")
print(f"{decompose(6)=}")
print(f"{decompose(7)=}")
print(f"{decompose(8)=}")
print(f"{decompose(9)=}")
print(f"{decompose(10)=}")