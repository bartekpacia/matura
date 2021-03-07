from reader import read_data

b = 2 ** 2 * 3 ** 2 * 5 ** 2 * 7 ** 2 * 13
ulamki = read_data()
# ulamki = [("1", "2"), ("2", "3"), ("5", "3"), ("2", "4"), ("15", "5")]

suma_ulamkow = 0
for ulamek in ulamki:
    licznik = int(ulamek[0])
    mianownik = int(ulamek[1])

    nowy_ulamek = (licznik * b) / mianownik
    suma_ulamkow += nowy_ulamek

print(f"{suma_ulamkow=}")
