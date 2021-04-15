from typing import Dict

from utils import jest_anagram

occurences: Dict[str, int] = {}
with open("dane_napisy.txt") as file:
    for line in file:
        splits = line.strip().split()
        a = splits[0]
        b = splits[1]

        # TODO
