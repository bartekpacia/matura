from utils import to_bin, to_hex, is_palindrome

with open("dane/dane.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(int("110101", 2))

bin_palindrome_count = 0
hex_palindrome_count = 0
for num in lines:
    num_bin = to_bin(num)
    num_hex = to_hex(num)

    if is_palindrome(str(num_bin)):
        bin_palindrome_count += 1

    if is_palindrome(str(num_hex)):
        hex_palindrome_count += 1

print(f"{bin_palindrome_count=}, {hex_palindrome_count=}")
