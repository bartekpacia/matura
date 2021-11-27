with open("dane.txt", "r") as f:
    liczby = [int(line) for line in f.readlines()]


def remove(k: int, nums_list: list[int]):
    i = k - 1  # Indeksacja od 0.

    while i < len(nums_list):
        del nums_list[i]
        i = i + (k - 1)


def gen_lucky_numbers(high: int) -> list[int]:
    lucky_nums = list(range(1, high + 1, 2))
    i = 1

    while True:
        if i < len(lucky_nums):
            remove_every_num = lucky_nums[i]
            if remove_every_num > len(lucky_nums):
                return lucky_nums
        else:
            return lucky_nums

        remove(remove_every_num, lucky_nums)
        i += 1


lucky_numbers = set(gen_lucky_numbers(10_000))

najdluzszy_ciag = []
for i, liczba1 in enumerate(liczby):
    obecny_ciag = []

    if liczba1 in lucky_numbers:
        obecny_ciag.append(liczba1)
    else:
        continue

    for j in range(i + 1, len(liczby)):
        liczba2 = liczby[j]

        if liczba2 in lucky_numbers:
            obecny_ciag.append(liczba2)
        else:
            if len(obecny_ciag) > len(najdluzszy_ciag):
                najdluzszy_ciag = obecny_ciag
                break

            obecny_ciag = []

print(f"{len(najdluzszy_ciag)}, pierwszy: {najdluzszy_ciag[0]}")
