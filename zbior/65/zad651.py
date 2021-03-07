frac_min = None

with open("dane_ulamki.txt") as f:
    for line in f:
        sline = line.strip()
        licznik, mianownik = map(int, sline.split())

        frac = licznik / mianownik

        if not frac_min:
            frac_min = frac

        if frac < frac_min:
            frac_min = frac
            print(f"new min frac: {licznik} / {mianownik} = {frac}")
