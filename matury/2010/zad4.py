with open("dane/anagram.txt") as f:
  lines = f.readlines()

odp_4a = open("odp_4a.txt", "w")
odp_4b = open("odp_4b.txt", "w")

def to_letters_dict(word) -> {}:
  letters = {}
  for char in word:
    if char not in letters:
      letters[char] = 1
    else:
      letters[char] += 1

  return letters

for line in lines:
  words = line.split()

  if max(words, key=len) == min(words, key=len):
    odp_4a.write(line)

  first_word = words[0]
  first_word_letters = to_letters_dict(first_word)

  all_same_length = True
  for i in range(1, len(words)):
    word = words[i]
    if first_word_letters != to_letters_dict(word):
      all_same_length = False
      break


  if all_same_length:
    odp_4b.write(line)


odp_4a.close()
odp_4b.close()
