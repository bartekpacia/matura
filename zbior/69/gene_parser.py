class Genotype:
    def __init__(self, genes: list[str], text: str) -> None:
        self.genes = genes
        self.text = text


def parse_genotype(text: str) -> Genotype:
    gene: str | None = None
    genes: list[str] = []

    for i, char in enumerate(text):
        if i + 1 >= len(text):
            break

        next_char = text[i + 1]
        if not gene and char == "A" and next_char == "A":
            gene = "AA"
        elif char == "B" and next_char == "B":
            if gene:
                gene += char
                gene += next_char
                genes.append(gene)
                gene = None
        else:
            if gene:
                gene += char

    return Genotype(genes=genes, text=text)
