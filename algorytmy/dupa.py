
import math

def gcd(a: int, b: int) -> int:
  while b != 0:
    # a, b = b, a % b
    temp = b
    b = a % b
    a = temp
  return a

def gcd_recursive(a: int, b: int) -> int:
  if (b == 0):
    return a
  return gcd_recursive(b, a % b)

def lcm(a: int, b: int) -> int:
  return (a * b) / gcd(a, b)

res4 = math.gcd(1, 4)
res3 = math.lcm(10, 5)
print(res4, res3)

res1 = gcd(4_000_000_000, 2)
res2 = gcd_recursive(4_000_000_000, 2)
print(res1, res2)