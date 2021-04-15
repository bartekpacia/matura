from gene_parser import parse_genotype

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]


max_gene_count = 0
max_gene_length = 0
for line in lines:
    genotype = parse_genotype(line)

    for g in genotype.genes:
        g_length = len(g)
        if g_length > max_gene_length:
            max_gene_length = g_length

    gene_count = len(genotype.genes)
    if gene_count > max_gene_count:
        max_gene_count = gene_count

print(f"{max_gene_count}, {max_gene_length}")
