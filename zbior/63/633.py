from typing import List

with open("ciagi.txt", "r") as f:
    ciagi = [int(line, 2) for line in f.readlines()]


def sito(n: int) -> List[int]:
    if n < 2:
        return list()

    arr = [True] * (n + 1)
    i = 2
    while i ** 2 < n:
        if arr[i]:
            j = i ** 2
            while j <= n:
                arr[j] = False
                j += i
        i += 1

    result = list()
    for i in range(2, n + 1):
        if arr[i]:
            result.append(i)

    return result


highest_num = 2 ** 18  # maksymalna długość ciągu
wszystkie_pierwsze = sito(highest_num)


def jest_polpierwsza(num: int) -> bool:
    for p in wszystkie_pierwsze:
        if num % p == 0 and (num / p) in wszystkie_pierwsze:
            return True

    return False


polpierwsze = []

for c in ciagi:
    if jest_polpierwsza(c):
        polpierwsze.append(c)

count_polpierwsze = len(polpierwsze)

low = 0
if polpierwsze:
    low = min(polpierwsze)

high = 0
if polpierwsze:
    high = max(polpierwsze)

print(f"{count_polpierwsze=}")
print(f"min polpierwsza: {low}")
print(f"max polpierwsza: {high}")
