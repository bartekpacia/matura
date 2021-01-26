with open("ciagi.txt", "r") as f:
    ciagi = [l.strip() for l in f.readlines()]


def ma_jedynki_obok_siebie(ten_ciag: str) -> bool:
    for i in range(1, len(ciag)):
        prev_char = ten_ciag[i - 1]
        current_char = ten_ciag[i]
        print(f"{prev_char=}, {current_char=}")
        if prev_char == "1" and current_char == "1":
            return True

    return False


count = 0
for ciag in ciagi:
    if not ma_jedynki_obok_siebie(ciag):
        count += 1

print(f"{count=}")
