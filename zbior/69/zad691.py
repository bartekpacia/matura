with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]

genes: dict[int, int] = {}
for line in lines:
    l = len(line)
    if l not in genes:
        genes[l] = 1
    else:
        genes[l] += 1

print(f"liczba gatunków: {len(genes)}")

maks = 0
for v in genes.values():
    if v > maks:
        maks = v

print(f"{maks=}")
