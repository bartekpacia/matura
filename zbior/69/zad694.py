from typing import List
from gene_parser import Gene, parse_genes

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def czy_odporny(genotyp: List[Gene]) -> bool:
    czesc_kodujaca = ""
    for g in genotyp:
        czesc_kodujaca += g.text

    return czesc_kodujaca == czesc_kodujaca[::-1]


def czy_silnie_odporny(genotyp: List[Gene]) -> bool:
    return True


odporne_count = 0
silnie_odporne_count = 0

for line in lines:
    genes: List[Gene] = parse_genes(line)

    odporny = czy_odporny(genes)
    if odporny:
        odporne_count += 1

    silnie_odporny = czy_silnie_odporny(genes)
    if silnie_odporny:
        silnie_odporne_count += 1

print(f"{odporne_count=}, {silnie_odporne_count=}")
