
def gcd(a: int, b: int) -> int:
  while b != 0:
    a, b = b, a % b
  return a

res = gcd(4_000_000_000, 2)
print(res)