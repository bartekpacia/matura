from utils import to_num_system, is_palindrome

with open("dane/dane.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

palindromes = {}
palindrome_bases = {}
for num in lines:
    num_palindrome_count = 0
    num_palindrome_bases = []
    for base in range(2, 17):
        n = to_num_system(num, base)

        if is_palindrome(n):
            num_palindrome_count += 1
            num_palindrome_bases.append(str(base))

    if num_palindrome_count:
        palindromes[num] = num_palindrome_count
        palindrome_bases[num] = num_palindrome_bases

count = 0
for num, v in sorted(palindromes.items(), key=lambda item: item[1], reverse=True):
    if count == 3:
        break

    bases = palindrome_bases[num]
    print(f"liczba {num} jest palindromem w {len(bases)} systemach:", ", ".join(bases))
    count += 1
