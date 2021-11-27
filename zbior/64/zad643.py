file = open("dane_obrazki.txt", "r")


def make_parity(row: list[int]):
    ones = 0
    for bit in row:
        if bit == 1:
            ones += 1

    # parzysta liczba jedynek
    if ones % 2 == 0:
        return 0

    return 1


cur_img_i = 0
cur_img: list[list[int]] = []
cur_row_i = 0
cur_errors_row = 0
cur_errors_col = 0
most_errors = 0

valid_imgs = 0
repairable_imgs = 0
unrepairable_imgs = 0
for line in file.readlines():
    line = line.strip()
    fmt_line = line.strip()[:-1]
    if fmt_line == "":
        cur_errors = cur_errors_row + cur_errors_col
        if cur_errors > most_errors:
            most_errors = cur_errors

        if cur_errors_col > 1 or cur_errors_row > 1:
            unrepairable_imgs += 1

        elif cur_errors_row == 1 or cur_errors_col == 1:
            repairable_imgs += 1

        else:
            valid_imgs += 1

        cur_img = []
        cur_row_i = 0
        cur_img_i += 1

        cur_errors_row = 0
        cur_errors_col = 0
        continue

    # parity row (19 bits)
    if len(fmt_line) != 20:
        parity_bits_col: list[int] = []
        for i in line:
            parity_bits_col.append(int(i))

        for i in range(20):
            cur_col: list[int] = []
            for j in range(20):
                cur_bit = int(cur_img[j][i])
                cur_col.append(cur_bit)

            if parity_bits_col[i] != make_parity(cur_col):
                cur_errors_col += 1

        continue

    # now the row is valid for sure (has 20 bits)
    # let's create a new list for the row we're traversing now
    cur_img.append([])

    for char in fmt_line:
        cur_img[cur_row_i].append(int(char))

    parity_bit = int(line[-1])
    calculated_parity_bit = make_parity(cur_img[cur_row_i])
    if calculated_parity_bit != parity_bit:
        cur_errors_row += 1

    cur_row_i += 1

file.close()

print(f"poprawne obrazki: {valid_imgs}")
print(f"naprawialne obrazki: {repairable_imgs}")
print(f"nienaprawialne obrazki: {unrepairable_imgs}")
print(f"najwięcej błędów: {most_errors}")
