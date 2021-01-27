def convert(n: int, d: int) -> str:
    digits = []

    while n > 0:
        n_temp = n // d
        digit = n % d
        digits.append(str(digit))
        n = n_temp

    return "".join(digits[::-1])


num = int(input("podaj liczbę (10): "))
div = int(input("podaj nową podstawę: "))

res = convert(num, div)

print(f"{num} w ({div}) to {res}")
