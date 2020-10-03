import caesar

output_file = open("wyniki_6_3.txt", "w")

two_words_list = []
with open("dane/dane_6_3.txt") as f:
  for line in f:
    two_words = line.strip().split()

    two_words_list.append(two_words)


for two_words in two_words_list:
  match = False
  for i in range(1, 27):
    encrypted = caesar.encrypt(two_words[0], i)

    if encrypted == two_words[1]:
      match = True

  if not match:
    output_file.write(f"{two_words[0]}\n")
