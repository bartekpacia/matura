with open("dane/liczby.txt") as f:
    lines = f.read().splitlines()

powers = set()
counter = 0

for i in range(0, 11):
    powers.add(3 ** i)

for ln in lines:
    if not ln:
        continue

    num = int(ln)
    if num in powers:
        counter += 1

print(f"znaleziono {counter} potęg 3")
