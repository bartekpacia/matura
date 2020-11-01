def wynik(i: int):
  if i < 3:
    return 1
  elif i % 2 == 0:
    return wynik(i - 3) + wynik(i - 1) + 1
  else:
    return wynik(i - 1) % 7

for i in range(2, 9):
  val = wynik(i)
  print(val)

W = []

for i in range(0, 1001):
    W.append(-1)


print("zad 1.3")

W[0] = 1
W[1] = 1
W[2] = 1
max_wart = 1

for i in range(3, 1001):
  if i % 2 == 0:
    W[i] = W[i - 3] + W[i - 1] + 1
  else:
    W[i] = W[i - 1] % 7
  
  if W[i] > max_wart:
    # max_wart = W[i]
    W[i] = max_wart

print(max_wart)
