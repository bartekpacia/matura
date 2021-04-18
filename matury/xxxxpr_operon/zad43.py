from utils import to_num_system, is_palindrome

with open("dane/dane.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

palindromes = {}
for num in lines:
    for base in range(2, 17):
        n = to_num_system(num, base)
        if is_palindrome(n):
            if not palindromes.get(base):
                palindromes[base] = 1
            else:
                palindromes[base] += 1

for base, v in sorted(palindromes.items()):
    print("podstawa", base, ":", v)
