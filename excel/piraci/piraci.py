import datetime

dni = 150
poczatek = datetime.date(1902, 10, 1)

dzisiaj = poczatek
coords_wigilia_str = None

coords = {"x": 0, "y": 0}
mile_na_polnoc = 0
dystans = 0  # całkowita przebyta odległość
dublony = 0
stracone_dublony = 0  # dublony stracone na rozrywki na Tortudze
dublony_zebrane_w_feralne_dni = 0
spotkani_zolnierze = 0

for dzien in range(1, dni + 1):
    nowe_dublony = 0
    # dodatkowe dublony każdego trzeciego dnia miesiąca
    if dzisiaj.day == 3:  # wychodzi na to, że dni są o jeden zaniżone
        nowe_dublony += 2
        print("Znaleziono dodatkowe 2 dublony!")

    coords["y"] += 8
    coords["x"] += 11
    mile_na_polnoc += 8
    dystans += (8 + 11)

    nowe_dublony += len(str(mile_na_polnoc))

    dublony += nowe_dublony
    coords["x"] -= nowe_dublony
    dystans += nowe_dublony

    # sobotnie hulanki
    if dzisiaj.isoweekday() == 6:
        print("SOBOTA")

        dublony_wydane_dzis = int(dublony * 0.1)

        dublony -= dublony_wydane_dzis
        stracone_dublony += dublony_wydane_dzis

    # wigilia 1902
    if dzisiaj == datetime.date(1902, 12, 24):
        coords_wigilia_str = coords_str
        print("Dzisiaj jest Wigilia!")

    # klątwa
    if nowe_dublony >= 4:
        dublony_zebrane_w_feralne_dni += nowe_dublony
        print("Klątwa...")

    # koniec logiki
    coords_str = str("x: " + str(coords["x"]) + "  y: " + str(coords["y"]))

    # wyświetlanie podsumowania dnia
    print("Dzień " + str(dzien) + " | " + str(dzisiaj))
    print("Przebyty dystans: " + str(dystans) +
          ", na północ: " + str(mile_na_polnoc))
    print("Nowe dublony: " + str(nowe_dublony))
    print("Dublony łącznie: " + str(dublony))
    print("Obóz w " + coords_str)
    print("- - - - - - - - - - - - - - - -")

    dzisiaj = dzisiaj + datetime.timedelta(1)

with open("wyniki_piraci.txt", "w") as f:
    # zadanie 1
    f.write("Wigilię 1902 roku piraci spędzili w miejscu o współrzędnych " +
            coords_wigilia_str + "\n")
    # zadanie 2
    f.write("Przez cały okres poszukiwań piraci przeszli " +
            str(dystans) + " mil\n")
    # zadanie 3
    f.write("Na Tortudze wydali łącznie " +
            str(stracone_dublony) + " dublonów\n")
    # zadanie 4
    f.write("Po powrocie na statek spotkali " +
            str(dublony_zebrane_w_feralne_dni) + " żołnierzy\n")
