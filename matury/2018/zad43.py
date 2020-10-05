lines = []
with open("dane/sygnaly.txt") as f:
  for l in f:
    lines.append(l.strip())


valid_lines = []
for line in lines:

  line_ok = True
  for char1 in line:
    for char2 in line:
      if abs(ord(char1) - ord(char2)) > 10:
        line_ok = False

  if line_ok:
    valid_lines.append(line)


for vl in valid_lines:
  print(vl)
