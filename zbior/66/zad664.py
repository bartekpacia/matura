def is_tri(a: int, b: int, c: int) -> bool:
    przeciw = max(a, b, c, )

    reszta = a + b + c - przeciw

    if reszta > przeciw:
        return True
    return False


liczba_trojkatow = 0
longest_seq = 0
with open("trojki.txt") as file:
    cur_seq = 0
    for line in file:
        a, b, c = map(int, line.strip().split())

        if is_tri(a, b, c):
            liczba_trojkatow += 1
            cur_seq += 1
        else:
            cur_seq = 0

        if cur_seq > longest_seq:
            longest_seq = cur_seq

print(f"{liczba_trojkatow=}, {longest_seq=}")
