from gene_parser import parse_genes

g = parse_genes("AADBAADDDDEEEBBEE")
print(g)
assert "AADBAADDDDEEEBB" == g
