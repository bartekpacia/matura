from gene_parser import parse_gene

with open("dane_geny.txt") as f:
    lines = [line.strip() for line in f.readlines()]

mutation_count = 0
for line in lines:
    gene = parse_gene(line)
    if "BCDDC" in gene:
        mutation_count += 1

print(f"{mutation_count=}")
