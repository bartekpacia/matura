with open("dane/dane.txt") as f:
    lines = []
    for line in f:
        sline = line.strip()
        lines.append(sline)

count = 0
biggest = int("10", 8)
smallest = int("2000001", 8)
for line in lines:
    line_num = int(line, 8)

    ok = True
    for i in range(len(line) - 1):
        num_current = int(line[i], 8)
        num_next = int(line[i + 1], 8)
        if not num_next >= num_current:
            ok = False

    if ok:
        count += 1
        if line_num > biggest:
            biggest = line_num
        elif line_num < smallest:
            smallest = line_num

print(f"{count=}, {smallest=}, {biggest=}")
