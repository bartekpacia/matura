with open("przyklad622.txt") as f:
  liczby2 = [int(l, 10) for l in f.readlines()]


print(len(liczby2))
longest_seq = []
for i in range(len(liczby2)):
  prev = liczby2[i]
  current_seq = []
  for j in range(i, len(liczby2)):
    num = liczby2[j]
    if num < prev:
      # break the sequence
      break
    current_seq.append(num)
  
  if len(current_seq) > len(longest_seq):
    longest_seq = current_seq


print(f"first element: {longest_seq[0]}, len: {len(longest_seq)}")
