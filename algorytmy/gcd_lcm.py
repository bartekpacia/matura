
import math

def gcd(a: int, b: int) -> int:
  while b != 0:
    print("-----")
    # a, b = b, a % b
    temp = b
    print(f"{a=},{b=},{temp=}")
    b = a % b
    print(f"{a=},{b=},{temp=}")
    a = temp
    print(f"{a=},{b=},{temp=}")
  return a

def gcd_recursive(a: int, b: int) -> int:
  if (b == 0):
    return a
  return gcd_recursive(b, a % b)

def lcm(a: int, b: int) -> int:
  return (a * b) / gcd(a, b)

res1 = gcd(963, 369)
print(res1)