import caesar

with open("dane/dane_6_1.txt") as f:
  slowa = [s.strip() for s in f.readlines()]


zaszyfrowane_slowa = []
for slowo in slowa:
  zaszyfrowane_slowo = caesar.encrypt(slowo, 107)

  zaszyfrowane_slowa.append(zaszyfrowane_slowo)

with open("wyniki_6_1.txt", "w") as f:
  for s in zaszyfrowane_slowa:
    f.write(f"{s}\n")