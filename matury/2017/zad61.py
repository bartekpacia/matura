input_file = open("dane/dane.txt")

bitmap = []
for line in input_file:
  pixels_str = line.strip().split()
  pixels_int = [int(p) for p in pixels_str]

  bitmap.append(pixels_int)

darkest = 255
brightest = 0
for i in range(len(bitmap)):
  for j in range(len(bitmap[i])):
    pixel = bitmap[i][j]

    if pixel < darkest:
      darkest = pixel

    if pixel > brightest:
      brightest = pixel

print(f"{brightest=}")
print(f"{darkest=}")
