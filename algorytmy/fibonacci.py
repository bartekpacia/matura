def fib_i(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    num1, num2 = 0, 1
    for i in range(n - 1):
        num1, num2 = num2, num1 + num2

    return num2


def fib_r(a):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    else:
        return fib_r(a - 1) + fib_r(a - 2)


for i in range(10):
    print(f"{i=}, {fib_r(i)=}")
