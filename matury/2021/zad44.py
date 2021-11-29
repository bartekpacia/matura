instrukcje: list[tuple[str, str]] = []
with open("dane/instrukcje.txt") as file:  # przyklad
    for i, line in enumerate(file):
        instrukcja = line.split()
        instrukcje.append((instrukcja[0], instrukcja[1]))

tekst: list[str] = []
for instrukcja in instrukcje:
    rodzaj = instrukcja[0]
    litera = instrukcja[1]

    if rodzaj == "DOPISZ":
        tekst.append(litera)
    elif rodzaj == "ZMIEN":
        tekst[-1] = litera
    elif rodzaj == "USUN":
        tekst.pop()
    elif rodzaj == "PRZESUN":
        index = 0
        for i, char in enumerate(tekst):
            if char == litera:
                index = i
                break

        if litera == "Z":
            nowa_litera = "A"
        else:
            nowa_litera = chr(ord(litera) + 1)

        tekst[index] = nowa_litera

print("".join(tekst))
