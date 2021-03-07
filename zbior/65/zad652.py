from reader import read_data

ulamki = read_data()


def nwd(a: int, b: int) -> bool:
    while b > 0:
        a, b = b, a % b

    return a


def wzglednie_pierwsze(a: int, b: int) -> bool:
    return nwd(a, b) == 1


count = 0
for ulamek in ulamki:
    licznik = int(ulamek[0])
    mianownik = int(ulamek[1])

    # ułamek jest nieskracalny, gdy licznik i mianownik
    # są względnie pierwsze
    if wzglednie_pierwsze(licznik, mianownik):
        count += 1

print(f"{count=}")
