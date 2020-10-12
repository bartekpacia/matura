palindromes = []

def is_palindrome(s: str) -> bool:
  reverse_s = []
  for c in reversed(s):
    reverse_s.append(c)

  return s == "".join(reverse_s)

with open("dane/hasla.txt") as f:
  for line in f:
    line = line.strip()

    if is_palindrome(line):
      palindromes.append(line)


with open("wynik4b.txt", "w") as f:
  for p in palindromes:
    f.write(f"{p}\n")