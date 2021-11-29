instrukcje: list[str] = []
with open("dane/instrukcje.txt") as file:
    for i, line in enumerate(file):
        rodzaj_instrukcji = line.split()[0]
        instrukcje.append(rodzaj_instrukcji)

najwieksza_dlugosc = 0
najwieksza_dlugosc_rodzaj = 0
for i in range(len(instrukcje)):
    rodzaj_instrukcji = instrukcje[i]
    dlugosc = 1
    for j in range(i + 1, len(instrukcje)):
        if instrukcje[j] == rodzaj_instrukcji:
            dlugosc += 1
        else:
            break

    if dlugosc > najwieksza_dlugosc:
        najwieksza_dlugosc = dlugosc
        najwieksza_dlugosc_rodzaj = rodzaj_instrukcji

print(najwieksza_dlugosc_rodzaj, najwieksza_dlugosc)
