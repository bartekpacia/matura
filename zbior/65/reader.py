def read_data() -> list[tuple[str, str, float]]:
    ulamki: list[tuple[str, str, float]] = []
    with open("dane_ulamki.txt") as f:
        for line in f:
            sline = line.strip()
            licznik, mianownik = sline.split()

            ulamek_wartosc = int(licznik) / int(mianownik)

            ulamek = (licznik, mianownik, ulamek_wartosc)
            ulamki.append(ulamek)

    return ulamki
