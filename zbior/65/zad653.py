from reader import read_data


def nwd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b

    return a


def wzglednie_pierwsze(a: int, b: int) -> bool:
    return nwd(a, b) == 1


def skroc(licznik: int, mianownik: int) -> tuple[int, int]:
    divider = 2
    while not wzglednie_pierwsze(licznik, mianownik):
        nowy_licznik = licznik / divider
        nowy_mianownik = mianownik / divider

        if nowy_licznik.is_integer() and nowy_mianownik.is_integer():
            licznik = nowy_licznik
            mianownik = nowy_mianownik
            divider = 1

        divider += 1

    return licznik, mianownik


ulamki = read_data()
# ulamki = [("1", "2"), ("2", "3"), ("5", "3"), ("2", "4"), ("15", "5")]

suma_licznikow = 0
for ulamek in ulamki:
    licznik = int(ulamek[0])
    mianownik = int(ulamek[1])

    if not wzglednie_pierwsze(licznik, mianownik):
        licznik, mianownik = skroc(licznik, mianownik)
        suma_licznikow += licznik
    else:
        suma_licznikow += licznik

print(f"{suma_licznikow=}")
