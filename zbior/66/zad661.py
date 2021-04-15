def sum_digits(num: int) -> int:
    nums = 0
    while num != 0:
        digit = num % 10
        nums += digit
        num = num // 10

    return nums


with open("trojki.txt") as file:
    for line in file:
        a, b, c = map(int, line.strip().split())

        if sum_digits(a) + sum_digits(b) == c:
            print(a, b, c)
