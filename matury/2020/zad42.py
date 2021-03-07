pairs = []
with open("dane/pary.txt") as f:
    for line in f:
        parsed_line = line.strip().split()

        num = int(parsed_line[0])
        text = parsed_line[1]

        pairs.append(tuple([num, text]))

pairs_result = []
for pair in pairs:
    same_chars_all = []

    word = pair[1]
    for i in range(len(word)):
        same_chars = []
        for j in range(i, len(word)):
            char1 = word[i]
            char2 = word[j]

            if char1 == char2:
                same_chars.append(char2)
            else:
                same_chars_all.append("".join(same_chars))
                break

            same_chars_all.append("".join(same_chars))

    longest = max(same_chars_all, key=len)
    pairs_result.append(longest)

with open("wyniki_4_2.txt", "w") as f:
    for pr in pairs_result:
        f.write(f"{pr} {len(pr)}\n")
