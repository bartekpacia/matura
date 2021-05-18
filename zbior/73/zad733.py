from importer import read_file

words = read_file()

samogloski = ["A", "E", "I", "O", "U", "Y"]


def jest_w_pyte(s1: str, s2: str) -> bool:
    return s1 not in samogloski and s2 not in samogloski


wyraz = "BCDDA"
words = [wyraz]

max_len_total = 0
for word in words:
    max_len = 0
    cur_len = 0
    for char in word:
        if char not in samogloski:
            cur_len += 1
        else:
            cur_len = 0

        if cur_len > max_len:
            max_len = cur_len

    if max_len > max_len_total:
        max_len_total = max_len

print("odp 1: ", max_len_total)
