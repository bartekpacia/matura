with open("dane.txt", "r") as f:
    liczby = [int(line) for line in f.readlines()]


def remove(remove_every_num: int, nums_list: list[int]):
    i = remove_every_num - 1  # Indeksacja od 0.

    while i < len(nums_list):
        del nums_list[i]
        i = i + (remove_every_num - 1)


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

lucky_count = 0
for liczba in liczby:
    if liczba in lucky_numbers:
        lucky_count += 1

print(f"{lucky_count=}")
