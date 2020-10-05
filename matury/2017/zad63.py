input_file = open("dane/dane.txt")

bitmap = []
for line in input_file:
  pixels_str = line.strip().split()
  pixels_int = [int(p) for p in pixels_str]

  bitmap.append(pixels_int)

contrasting_pixels = 0
for i in range(0, len(bitmap)):
  for j in range(0, len(bitmap[i])):
    contrasting = False
    pixel = bitmap[i][j]

    neighbours = []
    # upper
    if i > 0:
      neighbours.append(bitmap[i - 1][j])
    # lower
    if i < 199:
      neighbours.append(bitmap[i + 1][j])
    # left
    if j > 0:
      neighbours.append(bitmap[i][j - 1])
    # right
    if j < 319:
      neighbours.append(bitmap[i][j + 1])

    print(f"{i=}, {j=}, {len(neighbours)=}")


    for n in neighbours:
      if abs(pixel - n) > 128:
        contrasting = True

    if contrasting:
      contrasting_pixels += 1

print(f"{contrasting_pixels=}")

input_file.close()
