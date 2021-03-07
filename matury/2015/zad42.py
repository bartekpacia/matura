with open("dane/liczby.txt") as f:
    lines = [l.strip() for l in f.readlines()]

wynik42 = open("wynik42.txt", "w")

div_2 = 0
div_8 = 0
for line in lines:

    if line[-1] == "0":
        div_2 += 1

    if line[-1] == "0" and line[-2] == "0" and line[-3] == "0":
        div_8 += 1

wynik42.write(f"zadanie 4.2: {div_2} liczb podzielnych przez 2, {div_8} liczb podzielnych przez 8")
wynik42.close()
