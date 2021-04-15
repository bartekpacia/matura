from gene_parser import parse_gene

g = parse_gene("AADBAADDDDEEEBBEE")
print(g)
assert "AADBAADDDDEEEBB" == g
