input_file = open("dane/dane.txt")

bitmap = []
for line in input_file:
    pixels_str = line.strip().split()
    pixels_int = [int(p) for p in pixels_str]

    bitmap.append(pixels_int)

symmetric_rows_count = 0
for i in range(len(bitmap)):
    symmetric = True
    for j in range(len(bitmap[i])):
        left_pixel = bitmap[i][j]
        right_pixel = bitmap[i][319 - j]

        if left_pixel != right_pixel:
            symmetric = False
            break

    if symmetric:
        print(f"symetryczny wiersz {i=}")
        symmetric_rows_count += 1

rows_that_can_be_removed = len(bitmap) - symmetric_rows_count

print(f"{rows_that_can_be_removed=}")

input_file.close()
