with open("ciagi.txt", "r") as f:
    ciagi = [l.strip() for l in f.readlines()]


def jest_dwucykliczny(ciag: str) -> bool:
    if len(ciag) % 2 != 0:
        return False

    first_half = ciag[:(len(ciag) // 2)]
    second_half = ciag[len(ciag) // 2:]

    if first_half == second_half:
        return True
    return False


count = 0
for c in ciagi:
    if jest_dwucykliczny(c):
        count += 1
        print(c)

print(f"znaleziono {count} podciagow")
