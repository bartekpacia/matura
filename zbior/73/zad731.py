with open("tekst.txt") as f:
    text = f.readline().strip()

words = text.split()
print(len(words))
