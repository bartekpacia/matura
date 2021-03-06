nums_str = []
with open("dane/dane.txt") as f:
    lines = []
    for line in f:
        sline = line.strip()
        num = int(sline, 8)
        num_str = str(num)
        nums_str.append(num_str)

count = 0
for num_str in nums_str:
    if num_str[0] == num_str[-1]:
        count += 1

print(f"{count=}")
