file1 = open("dane_systemy1.txt")
file2 = open("dane_systemy2.txt")
file3 = open("dane_systemy3.txt")

lines1 = file1.readlines()
lines2 = file2.readlines()
lines3 = file3.readlines()

def parse(lines, base: int):
  min_temp = 99999999
  for line in lines:
    podzielona_linia = line.split()

    _ = int(podzielona_linia[0], base)
    temp = int(podzielona_linia[1], base)

    if temp < min_temp:
      min_temp = temp

  # jeśli może być zapisane z 0b
  print(f"{bin(min_temp)}")

  # jeśli ma być bez 0b to sie go pozbywamy
  # binarny_temp = bin(min_temp)
  # min_temp_bez_0b = binarny_temp.replace("0b", "")
  # print(f"{min_temp_bez_0b=}")

parse(lines1, 2)
parse(lines2, 4)
parse(lines3, 8)
