from reader import read_data

ulamki = read_data()

ulamek_min = None
for ulamek in ulamki:
    if not ulamek_min:
        ulamek_min = ulamek

    min_mianownik = int(ulamek_min[1])
    min_wartosc = ulamek_min[2]

    mianownik = int(ulamek[1])
    wartosc = ulamek[2]
    if wartosc < min_wartosc:
        ulamek_min = ulamek

    if wartosc == min_wartosc and mianownik < min_mianownik:
        ulamek_min = ulamek

print(f"{ulamek_min=}")
