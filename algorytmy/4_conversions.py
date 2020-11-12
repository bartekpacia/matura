#reprezentacja liczb w dowolnym systemie pozycyjnym
def hex(argument):
    if argument == 10:
        return "A"
    elif argument == 11:
        return "B"
    elif argument == 12:
        return "C"
    elif argument == 13:
        return "D"
    elif argument == 14:
        return "E"
    elif argument == 16:
        return "F"
    else:
      print(f"wrong {argument=} passed")
      return None

def convert(num: int, base: int) -> str:
    print(f"konwertuj({num=}, {base=})")

    if num == 0:
      return "0"
    if base < 2:

      return None

    res: str = ""

    while True:
        print(f"{num=} % {base=} = {num % base}")
        digit = num % base

        if digit > 9:
          digit = hex(digit)

        res += str(digit)

        num = num // base

        if num == 0:
          break

    return res[::-1]

n = int(input("Podaj liczbę do skonwertowania: "))
p = int(input("Podaj podstawę systemu do skonwertowania: "))

print(f"Liczba {n} w systemie {p}: ")

result = convert(n, p)
print(result)