from typing import List
from gene_parser import Gene, parse_genes

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]

genotypes: List[List[Gene]] = []
max_gene_count = 0
max_gene_length = 0
for line in lines:
    genes: List[Gene] = parse_genes(line)

    for g in genes:
        g_length = len(g.text)
        if g_length > max_gene_length:
            max_gene_length = g_length

    gene_count = len(genes)
    if gene_count > max_gene_count:
        max_gene_count = gene_count

    genotypes.append(genes)

print(f"{max_gene_count}, {max_gene_length}")
