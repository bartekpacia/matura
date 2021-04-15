from gene_parser import parse_genes

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]

mutation_count = 0
for line in lines:
    genes = parse_genes(line)

    all_genes = []
    for gene in genes:
        if "BCDDC" in gene.text:
            mutation_count += 1

print(f"{mutation_count=}")
