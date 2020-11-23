def fibonacci(n: int):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
  res = fibonacci(i)
  print(f"{i}: {res}")