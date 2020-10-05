lines = []
with open("dane/sygnaly.txt") as f:
  for l in f:
    lines.append(l.strip())


longest_unique_chars = 0
longest_unique_chars_word = ""
for line in lines:
  chars = {}
  for char in line:
    if char not in chars:
      chars[char] = 1

  unique_chars = len(chars.keys())
  if unique_chars > longest_unique_chars:
    longest_unique_chars = unique_chars
    longest_unique_chars_word = line

print(f"{longest_unique_chars_word} {longest_unique_chars}")
