def is_prime(num: int) -> bool:
  for i in range(2, num):
    if num % i == 0:
      return False

  return True


print(f"{is_prime(0)=}")
print(f"{is_prime(1)=}")
print(f"{is_prime(2)=}")
print(f"{is_prime(3)=}")
print(f"{is_prime(4)=}")
print(f"{is_prime(5)=}")