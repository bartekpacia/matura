def parse_gene(text: str) -> str:
    in_gene = False
    gene = ""

    for i, char in enumerate(text):
        if i + 1 >= len(text):
            break

        next_char = text[i + 1]
        if char == "A" and next_char == "A":
            in_gene = True
        elif char == "B" and next_char == "B":
            in_gene = False
            gene += char
            gene += next_char

        if in_gene:
            gene += char

    return gene
