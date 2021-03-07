valid_passwords = []

with open("dane/hasla.txt") as f:
    for line in f:
        line = line.strip()

        contains_2_chars = False
        for i in range(len(line) - 1):
            c1 = line[i]
            c2 = line[i + 1]

            if ord(c1) + ord(c2) == 220:
                print(f"{ord(c1)=} + {ord(c2)=} = 220")

                contains_2_chars = True
                break

        if contains_2_chars:
            valid_passwords.append(line)

with open("wynik4c.txt", "w") as f:
    for vp in valid_passwords:
        f.write(f"{vp}\n")
