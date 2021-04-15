from gene_parser import parse_genotype

g = parse_genotype("AADBAADDDDEEEBBEE")
print(g)
assert "AADBAADDDDEEEBB" == g
