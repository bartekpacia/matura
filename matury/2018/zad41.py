lines = []
with open("dane/sygnaly.txt") as f:
  for l in f:
    lines.append(l.strip())

message = []
for i in range(len(lines) + 1):
  print(i)
  if i != 0 and i % 40 == 0:
    letter = lines[i - 1][9]
    message.append(letter)

    print(f"{i=}, {letter=}")

print("".join(message))
