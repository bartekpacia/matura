with open("dane/dane.txt") as f:
    lines = []
    for line in f:
        sline = line.strip()
        lines.append(sline)
        print(sline)

# 52105

count = 0
for line in lines:
    if line[0] == line[-1]:
        count += 1

print(f"{count=}")
