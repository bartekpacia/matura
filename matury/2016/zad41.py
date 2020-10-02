punkty = []

with open("dane/punkty.txt") as f:
  punkty_raw = [l.strip() for l in f.readlines()]

  for p in punkty_raw:
    p = p.split()
    punkt = (int(p[0]), int(p[1]))

    punkty.append(punkt)

for p in punkty:
  print(p)