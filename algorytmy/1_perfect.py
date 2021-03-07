def is_perfect(num: int) -> bool:
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors) == num


print(f"{is_perfect(0)=}")
print(f"{is_perfect(1)=}")
print(f"{is_perfect(2)=}")
print(f"{is_perfect(3)=}")
print(f"{is_perfect(4)=}")
print(f"{is_perfect(5)=}")
print(f"{is_perfect(6)=}")
