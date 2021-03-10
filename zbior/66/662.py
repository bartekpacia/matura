def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    root = int(num ** 0.5) + 1
    for i in range(3, root, 2):
        if num % i == 0:
            return False

    return True


with open("trojki.txt") as file:
    for line in file:
        a, b, c = map(int, line.strip().split())

        if is_prime(a) and is_prime(b) and a * b == c:
            print(a, b, c)
