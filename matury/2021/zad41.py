dlugosc = 0
with open("dane/instrukcje.txt") as file:
    for line in file:
        if line.startswith("DOPISZ"):
            dlugosc += 1
        elif line.startswith("USUN"):
            dlugosc -= 1

print(dlugosc)
