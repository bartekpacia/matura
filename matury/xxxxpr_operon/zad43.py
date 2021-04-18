from utils import to_num_system, is_palindrome

with open("dane/dane.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

palindromes = {}
for num in lines:
    for i in range(2, 17):
        n = to_num_system(num, i)
        if is_palindrome(n):
            if not palindromes.get(i):
                palindromes[i] = 1
            else:
                palindromes[i] += 1

for p, v in sorted(palindromes.items()):
    print(p, v)
