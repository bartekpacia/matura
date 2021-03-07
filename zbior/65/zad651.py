from typing import List, Tuple

ulamki: List[Tuple[str, str, float]] = []

with open("dane_ulamki.txt") as f:
    for line in f:
        sline = line.strip()
        licznik, mianownik = sline.split()

        ulamek_wartosc = int(licznik) / int(mianownik)

        ulamek = (licznik, mianownik, ulamek_wartosc)
        ulamki.append(ulamek)

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
