input_file = open("dane/dane.txt")

bitmap = []
for line in input_file:
  pixels_str = line.strip().split()
  pixels_int = [int(p) for p in pixels_str]

  bitmap.append(pixels_int)

for i in range(len(bitmap)):
  for j in range(len(bitmap[i])):
    pixel = bitmap[i][j]

