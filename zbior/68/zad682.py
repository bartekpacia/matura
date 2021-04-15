from utils import jest_anagram

count = 0
with open("dane_napisy.txt") as file:
    for line in file:
        splits = line.strip().split()
        a = splits[0]
        b = splits[1]

        if jest_anagram(a, b):
            count += 1

print(f"{count=}")
