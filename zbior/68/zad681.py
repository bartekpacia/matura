from utils import jest_jednolity, jest_anagram

count = 0
with open("dane_napisy.txt") as file:
    for line in file:
        splits = line.strip().split()
        a = splits[0]
        b = splits[1]

        # can be simplified to:
        # if a == b:
        #   count += 1

        if jest_anagram(a, b) and jest_jednolity(a) and jest_jednolity(b):
            count += 1

print(f"{count=}")
