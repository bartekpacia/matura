from typing import List

with open("liczby2.txt") as f:
    liczby2 = [int(l.strip(), 10) for l in f.readlines()]

liczby2_whatif8 = []
with open("liczby2.txt") as f:
    for num in liczby2:
        num_in_oct = str(oct(num))[2:]
        print(num_in_oct)
        liczby2_whatif8.append(num_in_oct)


def count_six(input_liczby: List[int]) -> int:
    six_count = 0
    for i, num in enumerate(input_liczby):
        for c in str(num):
            if c == "6":
                six_count += 1

    return six_count


six_count_normal = count_six(liczby2)
six_count_whatif8 = count_six(liczby2_whatif8)

print(f"{six_count_normal=}, {six_count_whatif8=}")
