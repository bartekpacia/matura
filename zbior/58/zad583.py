dane1: list[int] = []
dane2: list[int] = []
dane3: list[int] = []


def load(filename: str, base: int) -> list[int]:
    file = open(filename)
    result: list[int] = []

    dane_systemy = [line.strip().split() for line in file.readlines()]

    for line in dane_systemy:
        # date = int(line[0], base)
        temp = int(line[1], base)

        result.append(temp)

    file.close()
    return result


def znajdz_dni_rekordowe(dane: list[int]) -> list[bool]:
    result: list[bool] = [False] * len(dane)  # True znaczy że jest to Rekordowy Dzień

    max_temp = dane[0]
    result[0] = True  # zgodnie z treścią zadania, pierwsza wartość też jest rekordem
    for i in range(len(dane)):
        temp = dane[i]

        if temp > max_temp:
            max_temp = temp
            result[i] = True

    return result


dane1 = load("dane_systemy1.txt", 2)
dane2 = load("dane_systemy2.txt", 4)
dane3 = load("dane_systemy3.txt", 8)

rekord1 = znajdz_dni_rekordowe(dane1)
rekord2 = znajdz_dni_rekordowe(dane2)
rekord3 = znajdz_dni_rekordowe(dane3)

rekordowe = 0
for i in range(len(dane1)):
    if rekord1[i] or rekord2[i] or rekord3[i]:
        rekordowe += 1

print(f"{rekordowe=}")
