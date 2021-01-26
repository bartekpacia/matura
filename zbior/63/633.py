with open("ciagi.txt", "r") as f:
    ciagi = [int(l, 2) for l in f.readlines()]

polpierwsze = []


def jest_polpierwsza(num: int) -> bool:
    for i in range((num // 2) + 1):
        for j in range((num // 2) + 1):
            pass


count_polpierwsze = 0

low = 0
if polpierwsze:
    low = min(polpierwsze)

high = 0
if polpierwsze:
    high = max(polpierwsze)

print(f"{count_polpierwsze=}")
print(f"min polpierwsza: {low}")
print(f"max polpierwsza: {high}")
