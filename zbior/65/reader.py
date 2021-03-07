from typing import List, Tuple


def read_data() -> List[Tuple[str, str, float]]:
    ulamki: List[Tuple[str, str, float]] = []
    with open("dane_ulamki.txt") as f:
        for line in f:
            sline = line.strip()
            licznik, mianownik = sline.split()

            ulamek_wartosc = int(licznik) / int(mianownik)

            ulamek = (licznik, mianownik, ulamek_wartosc)
            ulamki.append(ulamek)

    return ulamki
