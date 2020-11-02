with open("dane_systemy1.txt") as f:
  lines1 = f.readlines()

with open("dane_systemy2.txt") as f:
  lines2 = f.readlines()

with open("dane_systemy3.txt") as f:
  lines3 = f.readlines()

def data_ok(data):
  return (data - 12) % 24 == 0

pomiary_nie_ok = 0
for index, line1 in enumerate(lines1):
  line2 = lines2[index]
  line3 = lines3[index]

  podzielona_linia_1 = line1.split()
  podzielona_linia_2 = line2.split()
  podzielona_linia_3 = line3.split()

  data1 = int(podzielona_linia_1[0], 2)
  data2 = int(podzielona_linia_2[0], 4)
  data3 = int(podzielona_linia_3[0], 8)

  if not data_ok(data1) and not data_ok(data2) and not data_ok(data3):
    pomiary_nie_ok += 1

print(f"{pomiary_nie_ok=}")
