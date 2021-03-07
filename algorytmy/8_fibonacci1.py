def fib(n: int) -> int:
    n1, n2 = 0, 1
    n3 = 0
    for k in range(2, n + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return n3


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
