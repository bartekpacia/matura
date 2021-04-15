import operator

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]

genes = {}
for line in lines:
    l = len(line)
    if l not in genes:
        print(f"added {l}")
        genes[l] = 1
    else:
        print(f"juz jest {l}, kurwa")
        genes[l] += 1

print(f"liczba gatunków: {len(genes)}")

maks = 0
for v in genes.values():
    if v > maks:
        maks = v

print(f"{maks=}")
