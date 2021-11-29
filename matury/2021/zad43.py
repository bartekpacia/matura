instrukcje: list[tuple[str, str]] = []
with open("dane/instrukcje.txt") as file:  # przyklad
    for i, line in enumerate(file):
        instrukcja = line.split()
        instrukcje.append((instrukcja[0], instrukcja[1]))

dopisywane: dict[str, int] = {}
for instrukcja in instrukcje:
    rodzaj = instrukcja[0]
    if rodzaj == "DOPISZ":
        litera = instrukcja[1]
        if litera not in dopisywane:
            dopisywane[litera] = 1
        else:
            dopisywane[litera] += 1


max_dopisywane = 0
max_dopisywana_litera: str = "nic"

for litera, liczba in dopisywane.items():
    if liczba > max_dopisywane:
        max_dopisywane = liczba
        max_dopisywana_litera = litera

print(max_dopisywana_litera, max_dopisywane)
