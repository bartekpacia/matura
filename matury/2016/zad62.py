import caesar

input_file = open("dane/dane_6_2.txt")
output_file = open("wyniki_6_2.txt", "w")

for line in input_file:
    eword = line.strip().split()
    eword = tuple([eword[0], int(eword[1])])

    dword = caesar.decrypt(eword[0], eword[1])
    output_file.write(f"{dword}\n")

input_file.close()
output_file.close()
