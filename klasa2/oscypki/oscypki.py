from datetime import date, timedelta
from math import floor

liczba_owiec = 600
poczatek = date(2014, 4, 23)
koniec = date(2014, 9, 29)
dni = (koniec - poczatek).days + 1  # bo ostatni element range() jest wyłączny
dawane_mleko = 0.5
dzien_sezonu = 1
mleko_w_dniu = {}

cale_mleko = 0
wszystkie_serki = 0

print(f"Dni: {dni}")

for dzien in (poczatek + timedelta(n) for n in range(dni)):
    print(f"{dzien}, {dzien_sezonu} dzień sezonu")

    serki_dzis = 0
    if dzien_sezonu > 6:  # wyrób serka trwa 5 dni
        serki_dzis = floor(mleko_w_dniu[dzien_sezonu - 6] / 6)

    mleko_dzis = 0

    if dzien <= date(2014, 4, 29):
        mleko_dzis = 0.5

    elif dzien <= date(2014, 6, 24):
        if dzien_sezonu % 7 == 1:  # czy zaczął się już nowy tydzień?
            dawane_mleko = round(dawane_mleko * 1.04, 2)

    else:
        if dzien_sezonu % 7 == 1:
            dawane_mleko = round(dawane_mleko * 0.9, 2)

    cale_mleko_dzis = round(dawane_mleko * liczba_owiec, 2)
    mleko_w_dniu[dzien_sezonu] = cale_mleko_dzis

    cale_mleko += cale_mleko_dzis
    wszystkie_serki += serki_dzis

    print(f"Mleko od jednej owcy: {dawane_mleko}")
    print(f"Mleko od wszystkich owiec: {cale_mleko_dzis}")
    print(f"Serki: {serki_dzis}")
    print("----------------------------")
    dzien_sezonu += 1

print(f"Całe mleko: {cale_mleko}")
print(f"Wszystkie serki: {wszystkie_serki}")
