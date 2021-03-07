password_count = 200

even_num_of_chars = 0
with open("dane/hasla.txt") as f:
    for line in f:
        line = line.strip()

        if len(line) % 2 == 0:
            even_num_of_chars += 1

with open("wynik4a.txt", "w") as f:
    f.write(f"liczba hasel z parzysta liczba znakow: {even_num_of_chars}\n")
    f.write(f"liczba hasel z nieparzysta liczba znakow: {200 - even_num_of_chars}\n")
