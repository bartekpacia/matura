def fib(a):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)

for i in range(10):
    print(f"{i=}, {fib(i)=}")
