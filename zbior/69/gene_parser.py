from typing import List, Union


class Gene:
    def __init__(self, pos_start: int, pos_end: Union[int, None], text: str):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.text = text


class Genotype:
    def __init__(self, genes: List[Gene], text: str) -> None:
        self.genes = genes
        self.text = text


def parse_genotype(text: str) -> Genotype:
    gene = None
    genes: List[Gene] = []

    for i, char in enumerate(text):
        if i + 1 >= len(text):
            break

        next_char = text[i + 1]
        if not gene and char == "A" and next_char == "A":
            gene = Gene(i, None, "AA")
        elif char == "B" and next_char == "B":
            if gene:
                gene.text += char
                gene.text += next_char
                genes.append(gene)
                gene = None
        else:
            if gene:
                gene.text += char

    return Genotype(genes=genes, text=text)
