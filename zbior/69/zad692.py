from gene_parser import parse_genotype

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]

mutation_count = 0
for line in lines:
    genotype = parse_genotype(line)

    all_genes = []
    for gene in genotype.genes:
        if "BCDDC" in gene.text:
            mutation_count += 1

print(f"{mutation_count=}")
