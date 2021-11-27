import math

dane1: list[int] = []


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


dane1 = load("dane_systemy1.txt", 2)

skoki: list[int] = []
for i, ti in enumerate(dane1):
    for j in range(i + 1, len(dane1)):
        tj = dane1[j]

        r_ij = (ti - tj) ** 2

        skok = math.ceil((r_ij) / (abs(i - j)))
        skoki.append(skok)

najwiekszy_skok = max(skoki)
print(f"{najwiekszy_skok=}")
