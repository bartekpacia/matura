pairs: list[tuple[int, str]] = []
with open("dane/pary.txt") as f:
    for line in f:
        parsed_line = line.strip().split()

        num = int(parsed_line[0])
        text = parsed_line[1]

        t = (num, text)
        pairs.append(t)


def is_first_pair_smaller(pair1: tuple[int, str], pair2: tuple[int, str]) -> bool:
    if pair1[0] < pair2[0]:
        return True

    if pair1[0] == pair2[0]:
        if min(pair1[1], pair2[1]) == pair1[1]:
            return True

    return False


lowest_pair = (101, "a")
for pair in pairs:
    if pair[0] != len(pair[1]):
        continue

    if is_first_pair_smaller(pair, lowest_pair):
        lowest_pair = pair

print(f"{lowest_pair=}")
