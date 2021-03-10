def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    num1, num2 = 0, 1
    for i in range(n - 1):
        num1, num2 = num2, num1 + num2

    return num2

for i in range(10):
    print(f"{i=}, {fib(i)=}")
