from typing import List, Tuple

from reader import read_data


def nwd(a: int, b: int) -> bool:
    while b > 0:
        a, b = b, a % b

    return a


def wzglednie_pierwsze(a: int, b: int) -> bool:
    return nwd(a, b) == 1


def skroc(licz: int, mian: int) -> Tuple[int, int]:
    divider = 2
    while not wzglednie_pierwsze(licz, mian):
        new_licznik = licz / divider
        new_mianownik = mian / divider

        if new_licznik.is_integer() and new_mianownik.is_integer():
            licz = new_licznik
            mian = new_mianownik
            divider = 1

        divider += 1

    return licz, mian


ulamki = read_data()

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
