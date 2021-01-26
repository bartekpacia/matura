from typing import List

file = open("dane_obrazki.txt", "r")


def is_recursive(image) -> bool:
    if len(image) % 2 != 0 or len(image) != 20:
        return False

    for row in image:
        if len(row) != len(image):
            return False

    half = 10
    part1: List[int][int] = []
    part2: List[int][int] = []
    part3: List[int][int] = []
    part4: List[int][int] = []

    for row_i, row in enumerate(image):
        for col_i, _ in enumerate(row):
            if row_i < half and col_i < half:
                part1.append(row[:half])
            if row_i < half and col_i >= half:
                part2.append(row[half:])
            if row_i >= half and col_i < half:
                part3.append(row[:half])
            if row_i >= half and col_i >= half:
                part4.append(row[half:])

    if part1 == part2 and part2 == part3 and part3 == part4:
        return True
    return False


recursive_imgs = []
cur_img_i = 0
cur_img = []
cur_row_i = 0
rec_count = 0
for line in file.readlines():
    fmt_line = line.strip()[:-1]

    if fmt_line == "":
        if is_recursive(cur_img):
            recursive_imgs.append(cur_img)
            rec_count += 1

        cur_img = []
        cur_row_i = 0
        cur_img_i += 1
        continue

    if len(fmt_line) != 20:
        continue

    # now the row is good for sure
    cur_img.append([])

    for char in fmt_line:
        cur_img[cur_row_i].append(int(char))

    cur_row_i += 1

file.close()

print(f"liczba obrazków rekurencyjnych: {rec_count}")
print(f"pierwszy obrazek rekurencyjny:")
first_img = recursive_imgs[0]
for i, _ in enumerate(first_img):
    for j in first_img[i]:
        print(j, end="")
    print()
