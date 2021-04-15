from gene_parser import Genotype, parse_genotype

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def czy_odporny(genotyp: Genotype) -> bool:
    lewa_czesc_kodujaca = ""
    prawa_czesc_kodujaca = ""

    for g in genotyp.genes:
        lewa_czesc_kodujaca += g

    prawy_genotyp = parse_genotype(genotyp.text[::-1])
    for g in prawy_genotyp.genes:
        prawa_czesc_kodujaca += g

    return lewa_czesc_kodujaca == prawa_czesc_kodujaca


def czy_silnie_odporny(genotype: Genotype) -> bool:
    return genotype.text == genotype.text[::-1]


odporne_count = 0
silnie_odporne_count = 0

for line in lines:
    genotype = parse_genotype(line)

    odporny = czy_odporny(genotype)
    if odporny:
        odporne_count += 1

    silnie_odporny = czy_silnie_odporny(genotype)
    if silnie_odporny:
        silnie_odporne_count += 1

print(f"{odporne_count=}, {silnie_odporne_count=}")
